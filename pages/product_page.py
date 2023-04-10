from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    LOCATOR_PRODUCT_NAME = ((By.CLASS_NAME, 'name'))
    LOCATOR_ADD_TO_CART_BUTTON = (By.LINK_TEXT, 'Add to cart')

    def get_product_name_from_product_page(self):
        return self.find_element(self.LOCATOR_PRODUCT_NAME).text

    def click_to_add_to_cart(self):
        return self.find_element(self.LOCATOR_ADD_TO_CART_BUTTON).click()
