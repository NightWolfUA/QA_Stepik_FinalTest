from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    ADD_TO_CART = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.basket-mini")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BLOCK_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success > .alertinner > strong")
    MESSAGE_BLOCK_BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert-info > .alertinner > p strong")

