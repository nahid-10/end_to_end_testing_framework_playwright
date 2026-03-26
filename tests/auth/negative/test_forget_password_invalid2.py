from pages.auth.forget_password_page import ForgetPassword
from utils.helpers import load_json_data


def test_forget_password(page):
    
    data=load_json_data("test_data/data.json")
    
    email=data["forget_password_invalid2"]["email"]
    
    forget_password_obj=ForgetPassword(page)
    
    forget_password_obj.open()
    
    forget_password_obj.forget_password_page(email)
    
    result= forget_password_obj.get_message()
    
    assert "invalid" in result