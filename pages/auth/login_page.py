from pages.base_page import BasePage
from config.config import Config

class LoginPage(BasePage):
    
    #locators for login
    
    username="//input[@id='username']"
    password="//input[@id='password']"
    login_button="//button[@id='submit-login']"
    result_message="//div[@id='flash']"
    
    
    def open(self):
        self.navigate(f"{Config.base_url}/login")
        
    def login_page(self,username,password):
        self.fill(self.username,username)
        self.fill(self.password,password)
        self.click(self.login_button)
        
    def get_message(self):
        return self.get_text(self.result_message)