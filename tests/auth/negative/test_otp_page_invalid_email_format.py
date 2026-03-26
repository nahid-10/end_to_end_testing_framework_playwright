from pages.auth.otp_page import OtpPage
from utils.helpers import load_json_data

def test_otp_page(page):
    
    data=load_json_data("test_data/data.json")
    
    email=data["otp_invalid_email_format"]["email"]
    
    otp_page_obj=OtpPage(page)
    
    otp_page_obj.open()
    
    otp_page_obj.check_invalid_email_func(email)
    
    result=otp_page_obj.check_invalid_email_message_func()
    
    assert "Please enter a valid email address." in result