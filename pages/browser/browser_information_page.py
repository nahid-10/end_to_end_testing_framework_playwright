from pages.base_page import BasePage
from config.config import Config

class BrowserPage(BasePage):
    
    #locators for browserpage
    browser_information_button="//button[@id='browser-toggle']"
    
    def open(self):
        self.navigate(f"{Config.base_url}/my-browser")
        
    def browser_func(self):
        self.click(self.browser_information_button)
        
    