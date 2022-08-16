from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    EMAIL_USER = (By.ID, "id_login-username")
    PASSWORD_USER = (By.ID, "id_login-password")
    EMAIL_REGISTRATION_USER = (By.ID, "id_registration-email")
    PASSWORD_REGISTRATION_USER = (By.ID, "id_registration-password1")
    PASSWORD_REGISTRATION_USER2 = (By.ID, "id_registration-password2")

