from pages.base_page import BasePage
from config.config import Config

class ForgetPassword(BasePage):
    
    #locators for forget password
    email="//input[@id='email']"
    forget_password_button="//button[@type='submit']"
    result_message="//h1[.='Password reset page for Automation Testing Practice']"
    failed_message_loc="//div[@id='flash']"
    
    def open(self):
        self.navigate(f"{Config.base_url}/forgot-password")
        
    def forget_password_page(self,email):
        self.fill(self.email,email)
        self.click(self.forget_password_button)
        
    
    def get_message(self):
        return self.get_text(self.result_message)
    
    def failed_message(self):
        return self.get_text(self.failed_message_loc)