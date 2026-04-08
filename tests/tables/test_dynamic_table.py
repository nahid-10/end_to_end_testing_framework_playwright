from pages.tables.dynamic_table_page import DynamicTablePage
from utils.helpers import load_json_data

def test_dynamic_table(page):
    
    data=load_json_data("test_data/data.json")
    
    search=data["dynamic_table_valid"]["search"]
    value=data["dynamic_table_valid"]["value"]
    
    dynamic_table_obj=DynamicTablePage(page)
    
    dynamic_table_obj.open()
    
    dynamic_table_obj.dynamic_table_page_func(search,value)
    
    
    