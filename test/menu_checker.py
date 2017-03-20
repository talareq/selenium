import pytest
from selenium import webdriver



@pytest.fixture
def driver (request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    menu=driver.find_elements_by_css_selector("li#app-")
    for n in range(0,len(menu)):
        element = driver.find_elements_by_css_selector("li#app-")
        element[n].click()
        driver.find_elements_by_css_selector("h1#style")


