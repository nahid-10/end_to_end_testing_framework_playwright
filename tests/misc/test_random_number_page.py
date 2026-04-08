from pages.misc.random_number_page import RandomNumberPage


def test_random_number_visible(page):

    obj = RandomNumberPage(page)
    obj.open()

    number = obj.get_random_number()

    assert isinstance(number, float)