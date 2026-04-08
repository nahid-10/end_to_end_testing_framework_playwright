from pages.misc.about_page import AboutPage

def test_about_page(page):

    about_obj = AboutPage(page)

    about_obj.open()

    assert "Automation Testing Practice" in about_obj.get_heading_text()

    assert about_obj.is_welcome_text_visible()

    assert "Tawfik Nouri" in about_obj.get_author_name()

    assert "mailto:" in about_obj.get_email()

    assert about_obj.is_breadcrumb_visible()