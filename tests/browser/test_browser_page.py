from pages.browser.browser_information_page import BrowserPage
from utils.helpers import load_json_data


def test_brrowser_page(page):
    
    browser_page_obj=BrowserPage(page)
    
    browser_page_obj.open()
    
    browser_page_obj.browser_func()
    