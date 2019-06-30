from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), "Cart item is present, but should not be"

    def should_be_empty_cart_text(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_TEXT), "Empty cart text is not presented, cart is"\
                                                                           " not empty or there is no such element"
