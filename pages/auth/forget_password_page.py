from pages.base_page import BasePage
from config.config import Config

class ForgetPassword(BasePage):
    
    #locators for forget password
    email="//input[@id='email']"
    forget_password_button="//button[@class='btn btn-bg btn-primary d-block w-100']"
    result_message_backend="//div[@id='flash']"
    result_message_frontend="//div[@class='ms-1 invalid-feedback']"
    
    def open(self):
        self.navigate(f"{Config.base_url}/forgot-password")
        
    def forget_password_page(self,email):
        self.fill(self.email,email)
        self.click(self.forget_password_button)
        
    def get_message(self):
        return self.get_text(self.result_message_backend)
    
    def get_message2(self):
        return self.get_text(self.result_message_frontend)