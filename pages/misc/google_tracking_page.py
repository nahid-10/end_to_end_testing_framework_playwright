from pages.base_page import BasePage
from config.config import Config


class TrackingEventsPage(BasePage):

    # locators for tracking page
    click_button = "#click-event-btn"
    click_link = "#click-event-link"

    email_input = "#exampleFormControlInput1"
    message_input = "#exampleFormControlTextarea1"
    submit_button = "#submit-event-form button"

    conversion_button = "#conversion-event-btn"

    scrollable_div = "#scrollable-div"

    flash_message = "#flash"

    def open(self):
        self.navigate(f"{Config.base_url}/google-tracking-events")

    def click_event_button(self):
        self.click(self.click_button)

    def click_event_link(self):
        self.click(self.click_link)

    def submit_form(self, email, message):
        self.fill(self.email_input, email)
        self.fill(self.message_input, message)
        self.click(self.submit_button)

    def trigger_conversion(self):
        self.click(self.conversion_button)

    def scroll_inside_div(self):
        self.page.locator(self.scrollable_div).evaluate(
            "el => el.scrollTop = el.scrollHeight"
        )

    def get_flash_message(self):
        return self.get_text(self.flash_message)

    def is_flash_visible(self):
        return self.is_visible(self.flash_message)