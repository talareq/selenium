


def test_example(app, json_user):
    user = json_user
    app.login_admin()
    app.get("http://localhost/litecart/admin/?app=settings&doc=security")
    app.switch_captcha()
    app.get("http://localhost/litecart/en/create_account")
    app.litecard_helper.add_new(user)
    app.litecard_helper.login(user)
