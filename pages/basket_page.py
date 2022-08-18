from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        login_link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        login_link.click()

    def should_be_basket_status(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_STATUS), "Basket is no empty"
