from pages.base_page import BasePage
from config.config import Config


class RandomNumberPage(BasePage):

    random_number_text = "#randomNumber"

    def open(self):
        self.navigate(f"{Config.base_url}/random-number")

    def get_random_number(self):
        text = self.get_text(self.random_number_text)
        return float(text)

    def refresh_page(self):
        self.page.reload()