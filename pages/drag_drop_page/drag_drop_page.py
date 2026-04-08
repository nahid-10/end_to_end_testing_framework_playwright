from pages.base_page import BasePage
from config.config import Config

class DragDropPage(BasePage):

    source_div = "#source"
    target_div = "#target"

    def open(self):
        self.navigate(f"{Config.base_url}/drag-and-drop-circles")  

    def drag_item_to_target(self, color):
        
        source_locator = f"#source div.{color}"  
        target_locator = self.target_div

        self.page.locator(source_locator).drag_to(self.page.locator(target_locator))

    def is_item_in_target(self, color):
        
        target_locator = f"#target div.{color}"
        return self.page.locator(target_locator).count() > 0