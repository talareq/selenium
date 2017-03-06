import pytest
from selenium import webdriver

@pytest.fixture
def driver (request):

    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://www.google.com/")