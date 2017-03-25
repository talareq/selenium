



def test_example(app):
    app.litecard_helper.login_admin()
    app.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    app.get("http://localhost/litecart/admin/?app=countries&doc=edit_country")
    links=app.driver.find_elements_by_css_selector("i.fa.fa-external-link")
    for n in range(0,len(links)):
        current = app.driver.window_handles[0]
        Button = app.driver.find_elements_by_css_selector("i.fa.fa-external-link")
        Button[n].click()
        app.litecard_helper.wait_for_new_window()

        new_window = [window for window in app.driver.window_handles if window != current][0]
        app.driver.switch_to.window(new_window)
        app.driver.close()
        app.driver.switch_to_window(current)


