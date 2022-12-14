from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasketPageLocators


class MainPage(BasePage):
    def go_to_basket_page(self):
        login_link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        login_link.click()

    def should_be_basket_status(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_STATUS), "Basket is no empty"
