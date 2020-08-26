from .base_page import BasePage
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .locators import BasketPageLocators
from .locators import BasePageLocators
import time

class BasketPage(BasePage): 
    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CATALOG), "Basket is not empty"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE), "Message of empty basket is not presented"

    def should_be_item_page(self):
        item_page = self.browser.find_element(*BasePageLocators.ITEM_PAGE)
        item_page.click()