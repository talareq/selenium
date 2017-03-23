
def test_example(app):
    app.get("http://localhost/litecart/en/")

    app.litecard_helper.add_first_duck_to_cart()
    app.litecard_helper.add_first_duck_to_cart()
    app.litecard_helper.add_first_duck_to_cart()

    app.get("http://localhost/litecart/en/checkout")

    app.litecard_helper.remove_from_cart()







