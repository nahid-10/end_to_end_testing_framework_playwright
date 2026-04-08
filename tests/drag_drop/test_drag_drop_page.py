from pages.drag_drop_page.drag_drop_page import DragDropPage

def test_drag_drop_item(page):

    dragdrop = DragDropPage(page)
    dragdrop.open()

    
    dragdrop.drag_item_to_target("red")
    dragdrop.drag_item_to_target("green")
    dragdrop.drag_item_to_target("blue")

    
    assert dragdrop.is_item_in_target("red")
    assert dragdrop.is_item_in_target("green")
    assert dragdrop.is_item_in_target("blue")