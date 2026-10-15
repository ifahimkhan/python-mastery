import pytest

from course.l08_typing.practice.event_bus.event_bus import (
    EventBus,
    Mailer,
    OrderCancelled,
    OrderPlaced,
    Revenue,
    UserRegistered,
)


def test_handlers_get_only_their_event_type() -> None:
    bus, mailer, revenue = EventBus(), Mailer(), Revenue()
    bus.subscribe(UserRegistered, mailer.welcome)
    bus.subscribe(OrderPlaced, revenue.add)

    assert bus.publish(UserRegistered("ada")) == 1
    assert bus.publish(OrderPlaced(1, 500)) == 1
    assert bus.publish(OrderPlaced(2, 250)) == 1
    assert mailer.sent == ["welcome mail to ada"]
    assert revenue.total_cents == 750


def test_publishing_without_handlers_is_fine() -> None:
    assert EventBus().publish(OrderCancelled(1)) == 0


def test_handlers_run_in_subscription_order() -> None:
    bus, seen = EventBus(), []
    bus.subscribe(OrderCancelled, lambda event: seen.append(f"a{event.order_id}"))
    bus.subscribe(OrderCancelled, lambda event: seen.append(f"b{event.order_id}"))
    bus.publish(OrderCancelled(7))
    assert seen == ["a7", "b7"]


def test_unsubscribe() -> None:
    bus, seen = EventBus(), []
    stop = bus.subscribe(OrderCancelled, lambda event: seen.append(event.order_id))
    bus.publish(OrderCancelled(1))
    stop()
    stop()  # a second call does nothing
    bus.publish(OrderCancelled(2))
    assert seen == [1]


def test_a_handler_may_unsubscribe_itself_while_running() -> None:
    bus, seen = EventBus(), []

    def once(event: OrderCancelled) -> None:
        seen.append(event.order_id)
        stop()

    stop = bus.subscribe(OrderCancelled, once)
    bus.publish(OrderCancelled(1))
    bus.publish(OrderCancelled(2))
    assert seen == [1]


def test_failing_handlers_are_grouped_and_do_not_stop_others() -> None:
    bus, revenue = EventBus(), Revenue()

    def boom(event: OrderPlaced) -> None:
        raise ValueError(f"bad order {event.order_id}")

    bus.subscribe(OrderPlaced, boom)
    bus.subscribe(OrderPlaced, revenue.add)
    bus.subscribe(OrderPlaced, boom)

    with pytest.raises(ExceptionGroup) as caught:
        bus.publish(OrderPlaced(9, 100))
    assert [str(error) for error in caught.value.exceptions] == ["bad order 9", "bad order 9"]
    assert caught.value.exceptions[0].__notes__ == ["while handling OrderPlaced"]
    assert revenue.total_cents == 100
