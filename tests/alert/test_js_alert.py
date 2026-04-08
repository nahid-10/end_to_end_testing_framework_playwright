from pages.alert.js_alert_page import AlertPage
from utils.helpers import load_json_data

def test_js_alert(page):

    alert_obj = AlertPage(page)

    alert_obj.open()
    
    alert_obj.accept_alert()

    alert_obj.trigger_js_alert()