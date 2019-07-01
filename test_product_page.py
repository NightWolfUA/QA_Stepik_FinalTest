import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.cart_page import CartPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time

@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()


@pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"])
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"])
def test_message_dissapeared_after_adding_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_disappeare_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_empty_cart()
    cart_page.should_be_empty_cart_text()


@pytest.mark.login
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        self.browser = browser
        page = MainPage(self.browser, "http://selenium1py.pythonanywhere.com/")
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(self.browser, self.browser.current_url)
        login_page.register_new_user(str(time.time())+"@fakemail.org", '012qaz6789')
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        page = ProductPage(self.browser, self.link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self):
        page = ProductPage(self.browser, self.link)
        page.open()
        page.add_product_to_cart()
