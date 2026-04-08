from pages.elements.radio_button import RadioButtonPage
from utils.helpers import load_json_data

def test_select_radio_button(page):

    radio_obj = RadioButtonPage(page)

    radio_obj.open()
    
    radio_obj.select_color("red")

    assert radio_obj.is_color_selected("red")
    
    assert radio_obj.is_color_disabled("green")