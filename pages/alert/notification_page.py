from pages.base_page import BasePage
from config.config import Config

class NotificationMessagePage(BasePage):

    flash_message = "#flash b"
    close_button = "#flash .btn-close"

    def open(self):
        self.navigate(f"{Config.base_url}/notification-message")

    def get_message_text(self):
        return self.get_text(self.flash_message)

    def close_message(self):
        self.click(self.close_button)