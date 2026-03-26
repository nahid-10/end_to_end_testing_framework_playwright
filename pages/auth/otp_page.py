from pages.base_page import BasePage
from config.config import Config

class OtpPage(BasePage):
    
    #locators for otp page
    
    email="//input[@id='email']"
    invalid_email="//div[contains(@class,'invalid-feedback')]"
    send_otp_button="//button[@id='btn-send-otp']"
    enter_otp="//input[@id='otp']"
    verify_otp_button="//button[@id='btn-send-verify']"
    failed_message="//p[@id='otp-message']"
    success_mesasge="//div[@id='flash']"
    
    def open(self):
        self.navigate(f"{Config.base_url}/otp-login")
        
    def otp_page_func(self,email,otp):
        self.fill(self.email,email)
        self.click(self.send_otp_button)
        self.fill(self.enter_otp,otp)
        self.click(self.verify_otp_button)
        
    def check_invalid_email_func(self,email):
        self.fill(self.email,email)
        
    def check_invalid_email_message_func(self):
        return self.get_text(self.invalid_email)
    
    def get_success_message(self):
        return self.get_text(self.success_mesasge)
    
    def get_failed_message(self):
        return self.get_text(self.failed_message)