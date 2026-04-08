from pages.base_page import BasePage
from config.config import Config

class RadioButtonPage(BasePage):
    
    def open(self):
        self.navigate(f"{Config.base_url}/radio-buttons") 

    def select_color(self, color):
        locator = f"label[for='{color}']"
        self.click(locator)

    def is_color_selected(self, color):
        locator = f"input[name='color'][value='{color}']"
        return self.page.locator(locator).is_checked()

    def is_color_disabled(self, color):
        locator = f"input[name='color'][value='{color}']"
        return self.page.locator(locator).is_disabled()