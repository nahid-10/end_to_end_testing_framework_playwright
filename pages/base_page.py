from config.config import Config
import os
class BasePage:
    
    def __init__(self,page):
        self.page=page
        
    def navigate(self,url):
        self.page.goto(url)
    
    def click(self,locator):
        self.page.locator(locator).click()
        
    def fill(self,locator,text):
        self.page.locator(locator).fill(text)
    
    def screenshot(self, name):
        path = os.path.join(Config.SCREENSHOT_DIR, f"{name}.png")
        self.page.screenshot(path=path)
        
    def wait_for_element(self,locator):
        self.page.locator(locator).wait_for()
        
    def is_visible(self,locator):
        return self.page.locator(locator).is_visible()
    
    def get_text(self,locator):
        return self.page.locator(locator).inner_text()
    
        