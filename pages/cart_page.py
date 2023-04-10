from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    LOCATOR_PRODUCT_NAME_IN_CART = (By.XPATH, "//*[@id='tbodyid']/tr/td[2]")

    def get_product_name_in_cart(self):
        return self.find_element(self.LOCATOR_PRODUCT_NAME_IN_CART).text
