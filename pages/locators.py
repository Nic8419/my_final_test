from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    EMAIL_USER = (By.ID, "id_login-username")
    PASSWORD_USER = (By.ID, "id_login-password")
    EMAIL_REGISTRATION_USER = (By.ID, "id_registration-email")
    PASSWORD_REGISTRATION_USER = (By.ID, "id_registration-password1")
    PASSWORD_REGISTRATION_USER2 = (By.ID, "id_registration-password2")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_PRODUCT_IN_BASKET = (
    By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
