from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import _find_element
from selenium.webdriver.common.by import By


class LitecardHelper:

    def __init__(self, app):
        self.app = app


    def login_admin(self):
        driver = self.app.driver
        driver.get("http://localhost/litecart/admin/")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()

    def add_new(self, user):
        driver = self.app.driver
        self.change_field_value("firstname", user.firstname)
        self.change_field_value("lastname", user.lastname)
        self.change_field_value("address1", user.address1)
        self.change_field_value("postcode", user.postcode)
        self.change_field_value("city", user.city)
        self.change_field_value("email", user.email)
        self.change_field_value("email", user.email)
        self.change_field_value("phone", user.phone)
        self.change_field_value("password", user.password)
        select=driver.find_element_by_name("country_code")
        driver.execute_script("arguments[0].selectedIndex = 3", select)
        self.change_field_value("confirmed_password", user.password)
        driver.find_element_by_name("create_account").click()
        self.app.open_home_page()

    def login(self, user):
        driver = self.app.driver
        self.change_field_value("email", user.email)
        self.change_field_value("password", user.password)
        driver.find_element_by_name("login").click()


    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def check_exists_by_css(self, name):
        driver = self.app.driver
        try:
            driver.find_element_by_css_selector(name)
        except NoSuchElementException:
            return False
        return True

    def is_cart_empty(self):
        driver = self.app.driver
        try:
            driver.find_element_by_css_selector("a Back")
        except NoSuchElementException:
            return False
        return True

    def add_first_duck_to_cart(self):
        driver = self.app.driver
        driver.find_element_by_css_selector("li .image-wrapper").click()
        if self.check_exists_by_css("td .options") is True:
            select1 = driver.find_element_by_class_name("options")
            driver.execute_script("arguments[0].selectedIndex = 1", select1)
        driver.find_element_by_name("add_cart_product").click()
        text_before = driver.find_element_by_class_name("quantity").text
        wait = WebDriverWait(driver, 10)  # seconds
        wait.until(text_to_change((By.CLASS_NAME, "quantity"), text_before))
        driver.get("http://localhost/litecart/en/")

    def remove_from_cart(self):
        driver = self.app.driver
        driver.find_element_by_name("remove_cart_item").click()
        if self.is_cart_empty() is True:
            pass
        else:
            wait = WebDriverWait(driver, 10)  # seconds
            text_before = driver.find_element_by_id("order_confirmation-wrapper").text
            wait.until(text_to_change((By.ID, "order_confirmation-wrapper"), text_before))

class text_to_change(object):
    def __init__(self, locator, text):
            self.locator = locator
            self.text = text

    def __call__(self, driver):
            actual_text = _find_element(driver, self.locator).text
            return actual_text != self.text





