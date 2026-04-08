from pages.misc.google_tracking_page import TrackingEventsPage


def test_click_event(page):

    obj = TrackingEventsPage(page)
    obj.open()

    obj.click_event_button()


def test_submit_event(page):

    obj = TrackingEventsPage(page)
    obj.open()

    obj.submit_form(
        "nahid@test.com",
        "Testing submit event"
    )


def test_conversion_event(page):

    obj = TrackingEventsPage(page)
    obj.open()

    obj.trigger_conversion()


def test_scroll_event(page):

    obj = TrackingEventsPage(page)
    obj.open()

    obj.scroll_inside_div()


def test_flash_message(page):

    obj = TrackingEventsPage(page)
    obj.open()

    assert obj.is_flash_visible()