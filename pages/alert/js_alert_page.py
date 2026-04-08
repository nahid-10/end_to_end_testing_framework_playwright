from pages.base_page import BasePage
from config.config import Config

class AlertPage(BasePage):

    js_alert_button = "#js-alert"

    def open(self):
        self.navigate(f"{Config.base_url}/js-dialogs")  

    def trigger_js_alert(self):
        self.click(self.js_alert_button)

    def accept_alert(self):
        self.page.on("dialog", lambda dialog: dialog.accept())

    def get_alert_text(self):
        message_holder = {}

        def handle_dialog(dialog):
            message_holder["text"] = dialog.message
            dialog.accept()

        self.page.on("dialog", handle_dialog)

        self.click(self.js_alert_button)

        return message_holder["text"]