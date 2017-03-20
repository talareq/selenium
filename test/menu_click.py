import pytest
from selenium import webdriver

@pytest.fixture
def driver (request):
    #firefox_binary= FirefoxBinary("c:\\Program Files\\Nightly\\firefox.exe")
   # wd = webdriver.Firefox(firefox_binary=firefox_binary)
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://www.google.com/")