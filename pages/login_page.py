from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_link.click()
        assert "login" in self.browser.current_url, "Login in current url is not presented"

    def should_be_login_form(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()
        time.sleep(10)
    