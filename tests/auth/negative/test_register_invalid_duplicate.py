from pages.auth.register_page import RegisterPage
from utils.helpers import load_json_data
def test_register_invalid(page):
    
    data=load_json_data("test_data/data.json")
    
    username=data["register_invalid_duplicate"]["username"]
    password=data["register_invalid_duplicate"]["password"]
    confirm_password=data["register_invalid_duplicate"]["confirm_password"]
    
    register_obj=RegisterPage(page)
    
    register_obj.open()
    
    register_obj.register_page(username,password,confirm_password)
    
    result=register_obj.get_message()
    
    assert "try again" in result