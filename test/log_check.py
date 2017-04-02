

def test_example(app):
    app.login_admin()
    app.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    menu=app.driver.find_elements_by_css_selector("tr .row")
    for n in range(0,len(menu)):
        element = app.driver.find_elements_by_css_selector("tr .row")
        element[n].click()


        for l in app.driver.get_log("browser"):
            print(l)
        app.driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")