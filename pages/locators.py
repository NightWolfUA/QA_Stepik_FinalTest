from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators(object):
    ADD_TO_CART = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.basket-mini")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BLOCK_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert-success > .alertinner > strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[contains(@class,'alert-success')]/div[contains("
                                            "string(),'has been added to your basket.')]")
    MESSAGE_BLOCK_BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert-info > .alertinner > p strong")


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, 'span.btn-group > a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators(object):
    EMPTY_CART_TEXT = (By.XPATH, "//*[@id='content_inner']/p[contains(text(), 'Your basket is empty.')]")
    CART_ITEMS = (By.CSS_SELECTOR, 'div.basket-items')
