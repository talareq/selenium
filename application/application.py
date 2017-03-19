from lib2to3.pgen2 import driver

from selenium import webdriver
from helper.litecard_helper import LitecardHelper


class Application:

    def __init__(self):

        self.driver = webdriver.Firefox()
        self.litecard_helper = LitecardHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False


    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/litecart/en/")

    def destroy(self):
        self.wd.quit()

    def get(self, url):
        driver = self.driver
        driver.get(url)

    def login_admin(self):
        driver = self.driver
        driver.get("http://localhost/litecart/admin/")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()

    def switch_captcha(self):
        driver = self.driver
        driver.get("http://localhost/litecart/admin/?app=settings&doc=security&setting_group_key=store_info&page=1&action=edit&key=captcha_enabled")
        driver.find_element_by_xpath("//div/div/div/table/tbody/tr/td[3]/form/table/tbody/tr[7]/td[2]/label[2]").click()
        driver.find_element_by_name("save").click()

    def fill_field(self, field_name, text):
        driver.find_element_by_name(field_name).send_keys(text)


