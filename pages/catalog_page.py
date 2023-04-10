from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Catalog(BasePage):
    LOCATOR_PRODUCT_NAME = (By.CLASS_NAME, 'card-title')
    LOCATOR_CART_IN_HEADER_BUTTON = (By.ID, 'cartur')

    def click_to_product_name(self):
        return self.find_element(self.LOCATOR_PRODUCT_NAME).click()

    def get_product_name_from_catalog(self):
        return self.find_element(self.LOCATOR_PRODUCT_NAME).text

    def click_to_cart_button(self):
        return self.find_element(self.LOCATOR_CART_IN_HEADER_BUTTON).click()
