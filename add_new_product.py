def test_example(app):
    app.login_admin()
    app.get("http://localhost/litecart/admin/?category_id=0&app=catalog&doc=edit_product")
    app.fill_field(name[en], kaczka)