from pages.auth.register_page import RegisterPage
from utils.helpers import load_json_data


def test_register_invalid_short_password(page):
    
    data=load_json_data("test_data/data.json")
    
    username=data["register_invalid_short_password"]["username"]
    password=data["register_invalid_short_password"]["password"]
    confirm_password=data["register_invalid_short_password"]["confirm_password"]
    
    register_obj=RegisterPage(page)
    
    register_obj.open()
    
    register_obj.register_page(username,password,confirm_password)
    
    result=register_obj.get_message()
    
    assert "Password must be at least 4 characters long." in result