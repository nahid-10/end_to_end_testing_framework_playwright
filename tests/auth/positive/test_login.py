from pages.auth.login_page import LoginPage
from utils.helpers import load_json_data

def test_login(page):
    
    data=load_json_data("test_data/data.json")
    
    username=data["login_valid"]["username"]
    password=data["login_valid"]["password"]
    
    login_obj=LoginPage(page)
    
    login_obj.open()
    
    login_obj.login_page(username,password)
    
    result=login_obj.get_message()
    
    assert "You logged into a secure area" in result