

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
        self.change_field_value("postcode", user.postcode)
        self.change_field_value("city", user.city)
        self.change_field_value("email", user.email)
        self.change_field_value("password", user.password)
        self.change_field_value("confirmed_password", user.password)
        driver.find_element_by_name("create_account").click()
        self.app.open_home_page()

    def login(self, user):
        driver = self.app.driver
        self.change_field_value("email", user.email)
        self.change_field_value("password", user.password)
        driver.find_element_by_name("login").click()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)





