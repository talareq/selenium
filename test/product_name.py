import pytest
from selenium import webdriver

@pytest.fixture
def driver (request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/en/")
    products=driver.find_elements_by_css_selector("div#box-campaigns div.content")
    for n in range(0,len(products)):
        duck_title = driver.find_element_by_css_selector("div#box-campaigns .name").text
        duck_reg_price1 = driver.find_element_by_css_selector("div#box-campaigns .regular-price").text
        duck_red_price1 = driver.find_element_by_css_selector("div#box-campaigns .campaign-price").text
        driver.find_element_by_css_selector('img.image').click()

        duck_name = driver.find_element_by_css_selector("h1.title").text
        duck_reg_price2 = driver.find_element_by_css_selector(".regular-price").text
        duck_red_price2 = driver.find_element_by_css_selector(".campaign-price").text
        assert duck_title==duck_name
        assert duck_reg_price1==duck_reg_price2
        assert duck_red_price1==duck_red_price2
        driver.get("http://localhost/litecart/en/")
