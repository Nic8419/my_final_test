from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Is no login URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_USER), "Login Email form is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_USER), "Login Password form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.EMAIL_REGISTRATION_USER), "Registration Email form is not presented"
        assert self.is_element_present(
            *LoginPageLocators.PASSWORD_REGISTRATION_USER), "Registration Password form is not presented"
        assert self.is_element_present(
            *LoginPageLocators.PASSWORD_REGISTRATION_USER2), "Registration Password 2 form is not presented"
