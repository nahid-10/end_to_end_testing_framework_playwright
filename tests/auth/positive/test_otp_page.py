from pages.auth.otp_page import OtpPage
from utils.helpers import load_json_data

def test_otp_page(page):
    
    data=load_json_data("test_data/data.json")
    
    email=data["otp_valid"]["email"]
    otp=data["otp_valid"]["otp"]
    
    otp_page_obj=OtpPage(page)
    
    otp_page_obj.open()
    
    otp_page_obj.otp_page_func(email,otp)
    
    result=otp_page_obj.get_success_message()
    
    assert "You logged into a secure area!" in result