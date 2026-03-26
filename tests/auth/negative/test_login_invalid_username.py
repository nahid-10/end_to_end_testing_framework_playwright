from pages.auth.login_page import LoginPage
from utils.helpers import load_json_data

def test_login_invalid(page):
    
    data=load_json_data("test_data/data.json")
    
    username=data["login_invalid_username"]["username"]
    password=data["login_invalid_username"]["password"]
    
    login_obj=LoginPage(page)
    
    login_obj.open()
    
    login_obj.login_page(username,password)
    
    result=login_obj.get_message()
    
    assert "Your username is invalid!" in result