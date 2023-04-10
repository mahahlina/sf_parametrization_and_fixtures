import pytest
from selenium import webdriver
from pages.catalog_page import Catalog
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver
    # этот код выполнится после завершения теста
    driver.quit()


@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("Preparing some test data")


@pytest.fixture(scope="class")
def catalog(browser):
    catalog = Catalog(browser)
    return catalog


@pytest.fixture(scope="class")
def product(browser):
    product = ProductPage(browser)
    return product


@pytest.fixture(scope="class")
def cart(browser):
    cart = CartPage(browser)
    return cart
