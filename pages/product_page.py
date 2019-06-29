from .base_page import BasePage
from .locators import ProductPageLocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def add_product_to_cart(self):
        button_add_to_cart_link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button_add_to_cart_link.click()
        self.solve_quiz_and_get_code()
        self.product_name_should_be_in_message()
        self.basket_price_should_be_equal_to_product_price()

    def product_name_should_be_in_message(self):
        try:
            WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.MESSAGE_BLOCK_PRODUCT_NAME))
            message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_BLOCK_PRODUCT_NAME)
            product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
            assert message_product_name.text == product_name.text, "Product names are not equal"
        except TimeoutException:
            assert False, "There is no message with product name about successful add to cart"

    def basket_price_should_be_equal_to_product_price(self):
        try:
            WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.MESSAGE_BLOCK_BASKET_PRICE))
            product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
            basket_price = self.browser.find_element(*ProductPageLocators.MESSAGE_BLOCK_BASKET_PRICE)
            assert product_price.text == basket_price.text, "Prices are not equal"
        except TimeoutException:
            assert False, "There is no message with basket price after add to cart"
