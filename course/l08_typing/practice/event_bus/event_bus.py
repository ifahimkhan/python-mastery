"""
=====================================================================
 PRACTICE 08.B - A typed event bus
=====================================================================
 GOAL   : Let parts of a program talk through events without knowing
          each other, with mypy checking that every handler accepts the
          event type it subscribed to.
 RUN    : uv run python -m course.l08_typing.practice.event_bus.event_bus
 OUTPUT :
          UserRegistered handlers run: 1
          OrderPlaced handlers run: 3
          after unsubscribe: 2
          nobody listens to OrderCancelled: 0
          1 handler(s) failed: order 3 needs manual review (while handling OrderPlaced)
          mails: ['welcome mail to ada']
          revenue cents: 253500 (the failing handler did not stop it)
          log: ['order 1']
 DESIGN : subscribe[E](event_type: type[E], handler: Callable[[E], None])
          ties the handler's parameter to the event class, so mypy
          rejects a handler for the wrong event. Inside, the dict can't
          express "each key has its own value type", so it stores
          Callable[[Any], None]; only subscribe() can add to it, which
          keeps that one Any safe. A failing handler doesn't stop the
          others: all errors are raised together as an ExceptionGroup.
 EXTEND : Deliver an event to handlers of its base classes too
          (walk type(event).__mro__).
=====================================================================
"""

from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class UserRegistered:
    username: str


@dataclass(frozen=True)
class OrderPlaced:
    order_id: int
    total_cents: int


@dataclass(frozen=True)
class OrderCancelled:
    order_id: int


class EventBus:
    def __init__(self) -> None:
        self._handlers: defaultdict[type, list[Callable[[Any], None]]] = defaultdict(list)

    def subscribe[E](self, event_type: type[E], handler: Callable[[E], None]) -> Callable[[], None]:
        """Register a handler. Returns a function that unsubscribes it."""
        self._handlers[event_type].append(handler)

        def unsubscribe() -> None:
            handlers = self._handlers[event_type]
            if handler in handlers:
                handlers.remove(handler)

        return unsubscribe

    def publish(self, event: object) -> int:
        """Call every handler for exactly this event type. Returns how many ran."""
        handlers = list(self._handlers.get(type(event), []))  # a copy: handlers may unsubscribe
        errors: list[Exception] = []
        for handler in handlers:
            try:
                handler(event)
            except Exception as error:
                error.add_note(f"while handling {type(event).__name__}")
                errors.append(error)
        if errors:
            raise ExceptionGroup(f"{len(errors)} handler(s) failed", errors)
        return len(handlers)


@dataclass
class Mailer:
    sent: list[str] = field(default_factory=list)

    def welcome(self, event: UserRegistered) -> None:
        self.sent.append(f"welcome mail to {event.username}")


@dataclass
class Revenue:
    total_cents: int = 0

    def add(self, event: OrderPlaced) -> None:
        self.total_cents += event.total_cents


def fail_on_big_orders(event: OrderPlaced) -> None:
    if event.total_cents > 100_000:
        raise ValueError(f"order {event.order_id} needs manual review")


def main() -> None:
    bus = EventBus()
    mailer, revenue = Mailer(), Revenue()
    log: list[str] = []

    bus.subscribe(UserRegistered, mailer.welcome)
    bus.subscribe(OrderPlaced, revenue.add)
    bus.subscribe(OrderPlaced, fail_on_big_orders)
    stop_logging = bus.subscribe(OrderPlaced, lambda event: log.append(f"order {event.order_id}"))
    # bus.subscribe(OrderPlaced, mailer.welcome)
    # mypy: Argument 2 to "subscribe" of "EventBus" has incompatible type
    #       "Callable[[UserRegistered], None]"; expected "Callable[[OrderPlaced], None]"

    print("UserRegistered handlers run:", bus.publish(UserRegistered("ada")))
    print("OrderPlaced handlers run:", bus.publish(OrderPlaced(1, 2_500)))
    stop_logging()
    print("after unsubscribe:", bus.publish(OrderPlaced(2, 1_000)))
    print("nobody listens to OrderCancelled:", bus.publish(OrderCancelled(1)))

    try:
        bus.publish(OrderPlaced(3, 250_000))
    except ExceptionGroup as group:
        for error in group.exceptions:
            print(f"{group.message}: {error} ({error.__notes__[0]})")

    print("mails:", mailer.sent)
    print("revenue cents:", revenue.total_cents, "(the failing handler did not stop it)")
    print("log:", log)


if __name__ == "__main__":
    main()
