from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import _find_element


class text_to_change(object):
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text

    def __call__(self, driver):
        actual_text = _find_element(driver, self.locator).text
        return actual_text != self.text



def test_example(app):
    app.get("http://localhost/litecart/en/")
    app.driver.find_emelemnt_by_css_selector("li .product").click()
    if len(app.driver.find_element_by_class_name("options[Size]")) > 0:
        select1 = app.driver.find_element_by_class_name("options")
        app.driver.execute_script("arguments[0].selectedIndex = 2", select1)
    app.driver.find_emelemnt_by_name("add_cart_product").click()
    text_before = app.driver.find_element_by_class_name("quantity").text
    wait = WebDriverWait(app.driver, 10)  # seconds
    wait.until(text_to_change((By.CLASS_NAME, "quantity"), text_before))
    app.get("http://localhost/litecart/en/")
    app.driver.find_emelemnt_by_css_selector("li .product").click()
    if len(app.driver.find_element_by_class_name("options[Size]")) > 0:
        select1 = app.driver.find_element_by_class_name("options")
        app.driver.execute_script("arguments[0].selectedIndex = 2", select1)
    app.driver.find_emelemnt_by_name("add_cart_product").click()
    text_before = app.driver.find_element_by_class_name("quantity").text
    wait.until(text_to_change((By.CLASS_NAME, "quantity"), text_before))
    app.get("http://localhost/litecart/en/")
    app.driver.find_emelemnt_by_css_selector("li .product").click()
    if len(app.driver.find_element_by_class_name("options[Size]")) > 0:
        select1 = app.driver.find_element_by_class_name("options")
        app.driver.execute_script("arguments[0].selectedIndex = 2", select1)
    app.driver.find_emelemnt_by_name("add_cart_product").click()
    text_before = app.driver.find_element_by_class_name("quantity").text
    wait.until(text_to_change((By.CLASS_NAME, "quantity"), text_before))
    app.driver.find_emelemnt_by_css_selector("a Checkout").click()
    duck_list = app.driver.find_emelemnts_by_css_selector("li .shortcut")
    for element in duck_list:
        element.app.driver.find_element_by_css_selector(".inact").click()
        app.driver.find_element_by_name("remove_cart_item").click()
        wait.until(text_to_change((By.ID, "order_confirmation-wrapper"), text_before))
    if len(app.driver.find_element_by_name("remove_cart_item")) > 0:
        app.driver.find_element_by_name("remove_cart_item").click()
        wait.until(text_to_change((By.ID, "order_confirmation-wrapper"), text_before))



