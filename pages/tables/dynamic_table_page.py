from config.config import Config
from pages.base_page import BasePage

class DynamicTablePage(BasePage):
    
    search="//input[@type='search']"
    next_button=".page-link[data-dt-idx*='next']"
    dropdown_length = "select[name='example_length']"
    
    
    
    def open(self):
        self.navigate(f"{Config.base_url}/dynamic-pagination-table")

    def dynamic_table_page_func(self,search_input, value):
        self.fill(self.search,search_input)
        self.locate(self.dropdown_length).select_option(value)
        
    