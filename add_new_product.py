def test_example(app):
    app.login_admin()
    app.get("http://localhost/litecart/admin/?category_id=0&app=catalog&doc=edit_product")
    app.litecard_helper.change_field_value("name[en]", "kaczka")
    app.driver.find_element_by_xpath("//ul[@class='index']//a[.='Information']").click()
    select1=app.driver.find_element_by_name("manufacturer_id")
    app.driver.execute_script("arguments[0].selectedIndex = 1", select1)
    select2 = app.driver.find_element_by_name("supplier_id")
    app.driver.execute_script("arguments[0].selectedIndex = 1", select2)
    app.litecard_helper.change_field_value("keywords", "kaczka")
    app.driver.find_element_by_xpath("//ul[@class='index']//a[.='Prices']").click()
    app.litecard_helper.change_field_value("purchase_price", "20,00")
    select3= app.driver.find_element_by_name("purchase_price_currency_code")
    app.driver.execute_script("arguments[0].selectedIndex = 1", select3)
    app.driver.find_element_by_name("save").click()

    duck_list = app.driver.find_elements_by_css_selector(".dataTable")

    if str("kaczka") in duck_list:
        pass