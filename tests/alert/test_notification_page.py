from pages.alert.notification_page import NotificationMessagePage
from playwright.sync_api import expect

def test_notification_message(page):
    notification = NotificationMessagePage(page)
    notification.open()
    
    
    assert notification.get_message_text() in ["Action successful", "Action unsuccessful, please try again"]
    
    
    notification.close_message()
    expect(page.locator(notification.flash_message)).to_be_hidden()
    
    
    notification.open()
    assert notification.get_message_text() in ["Action successful", "Action unsuccessful, please try again"]