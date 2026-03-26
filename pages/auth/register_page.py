from config.config import Config
from pages.base_page import BasePage


class RegisterPage(BasePage):
    
    #locator for registration
    
    username="//input[@id='username']"
    password="//input[@id='password']"
    confirm_password="//input[@id='confirmPassword']"
    register_button="//button[@class='btn btn-bg btn-primary d-block w-100']"
    
    result_message="//div[@id='flash']"
    
    def open(self):
        self.navigate(f"{Config.base_url}/register")
        
    def register_page(self,username,password,confirm_password):
        self.fill(self.username,username)
        self.fill(self.password,password)
        self.fill(self.confirm_password,confirm_password)
        self.click(self.register_button)
    
    def get_message(self):
        return self.get_text(self.result_message)