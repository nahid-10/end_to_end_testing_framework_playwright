from pages.auth.register_page import RegisterPage
from utils.helpers import load_json_data

def test_register(page):
    data=load_json_data("test_data/data.json")
    
    username=data["register_valid"]["username"]
    password=data["register_valid"]["password"]
    confirm_password=data["register_valid"]["confirm_password"]
    
    register_obj=RegisterPage(page)
    
    register_obj.open()
    
    register_obj.register_page(username,password,confirm_password)
    
    result = register_obj.get_message()
    
    assert "Successfully registered" in result