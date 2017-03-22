from selenium.webdriver.support.wait import WebDriverWait
from helper.litecard_helper import text_to_change
from selenium.webdriver.common.by import By






def test_example(app):
    app.get("http://localhost/litecart/en/")

    app.litecard_helper.add_first_duck_to_cart()
    app.litecard_helper.add_first_duck_to_cart()
    app.litecard_helper.add_first_duck_to_cart()

    app.get("http://localhost/litecart/en/checkout")

    app.litecard_helper.remove_from_cart()
    app.litecard_helper.remove_from_cart()
    app.litecard_helper.remove_from_cart()






