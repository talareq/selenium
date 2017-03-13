import pytest
from selenium import webdriver

@pytest.fixture
def driver (request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get(" http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_css_selector('a[href="http://localhost/litecart/admin/?app=countries&doc=countries"]').click()
    table=driver.find_elements_by_css_selector("tr.row")
    countries=get_countries_list(table)
    sorted_countries=alphabetical(table)
    assert countries == sorted_countries
    driver.find_element_by_css_selector(
        'a[href="http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones"]').click()
    geo_zones_table=driver.find_elements_by_css_selector("tr.row")
    geo_zones=get_countries_list(geo_zones_table)
    geo_zones_sorted=alphabetical(geo_zones_table)
    assert geo_zones == geo_zones_sorted

    for row in table:

        cells=row.find_elements_by_tag_name("td")
        zone=cells[5].text

        for zone != 0:
            cells = row.find_elements_by_tag_name("td")
            cells[4].click
            country_list=driver.find_element_by_id("table-zones")
            zone_countries=get_countries_list(country_list)
            sorted_zone_countries=alphabetical(zone_countries)
            assert zone_countries == sorted_zone_countries
            driver.find_element_by_css_selector(
                'a[href="http://localhost/litecart/admin/?app=countries&doc=countries"]').click()













def alphabetical(table):
    countries = get_countries_list(table)
    return sorted(countries)

def get_countries_list(table):
    countries = []
    for row in table:
        cells = row.find_elements_by_tag_name("td")
        name = cells[4].text
        countries.append(name)

    return countries
