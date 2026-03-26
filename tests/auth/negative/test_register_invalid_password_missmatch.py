from pages.auth.register_page import RegisterPage
from utils.helpers import load_json_data


def test_register_invalid_password_missmatch(page):
    
    data=load_json_data("test_data/data.json")
    
    username=data["register_invalid_password_mismatch"]["username"]
    password=data["register_invalid_password_mismatch"]["password"]
    confirm_password=data["register_invalid_password_mismatch"]["confirm_password"]
    
    register_obj=RegisterPage(page)
    
    register_obj.open()
    
    register_obj.register_page(username,password,confirm_password)
    
    result=register_obj.get_message()
    
    assert "Passwords do not match" in result