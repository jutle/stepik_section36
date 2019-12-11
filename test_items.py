import time
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_is_present(browser):
    browser.get(link)

    try:
        browser.find_elements_by_css_selector(".btn-add-to-basket")
        button_is_present = True
    except NoSuchElementException:
        button_is_present = False

    assert button_is_present is True, "Unable to locate 'Add to basket' button"

# time.sleep(30)

