
class TestUi:
    def test_view_product_card(self, browser, product, catalog):
        product.go_to_site()
        name1 = catalog.get_product_name_from_catalog()
        catalog.click_to_product_name()
        name_2 = product.get_product_name_from_product_page()
        assert name1 == name_2

    def test_add_product_to_cart(self, browser, product, catalog, cart):
        product.go_to_site()
        catalog.click_to_product_name()
        name_1 = product.get_product_name_from_product_page()
        product.click_to_add_to_cart()
        catalog.click_to_cart_button()
        name_2 = cart.get_product_name_in_cart()
        assert name_1 == name_2
