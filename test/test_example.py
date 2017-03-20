import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


@pytest.fixture
def driver (request):
    #firefox_binary= FirefoxBinary("c:\\Program Files\\Nightly\\firefox.exe")
   # wd = webdriver.Firefox(firefox_binary=firefox_binary)
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd



def test_example(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnG").click()
    WebDriverWait(driver, 10).until(EC.title_is("webdriver"))