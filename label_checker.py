import pytest
from selenium import webdriver

@pytest.fixture
def driver (request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/en/")
    driver.find_element_by_css_selector(".category-1").click()
    products=driver.find_elements_by_css_selector("div.content")
    #for element in products:
    stickernew=driver.find_elements_by_css_selector("div.sticker.new")
    stickersale=driver.find_elements_by_css_selector("div.sticker.sale")
    assert len(products)==len(stickernew+stickersale)