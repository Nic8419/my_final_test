from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        name_of_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        btn.click()
        self.solve_quiz_and_get_code()
        assert name_of_product == self.browser.find_element(
            *ProductPageLocators.NAME_PRODUCT_IN_BASKET).text, "The name of the product in the basket is different"

    def price_should_be_same_as_checked(self):
        price_of_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        btn.click()
        self.solve_quiz_and_get_code()
        assert price_of_product in self.browser.find_element(
            *ProductPageLocators.PRICE_PRODUCT_IN_BASKET).text, "The Price of the product in the basket is different"
