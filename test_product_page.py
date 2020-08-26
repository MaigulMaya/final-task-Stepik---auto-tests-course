from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException
import time
import pytest

#def test_guest_should_see_login_link_on_product_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page = ProductPage(browser, link)
 #   page.open()
  #  page.should_be_login_link()

#def test_guest_can_go_to_login_page_from_product_page(browser):
 #   link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
  #  page = ProductPage(browser, link)
   # page.open()
    #page.go_to_login_page()

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
 #                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
  #                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
   #                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
     #                             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
      #                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
       #                           pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
        #                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         #                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

#def test_guest_can_add_product_to_basket(browser, link):
 #   page = ProductPage(browser, link)
  #  page.open()
   # page.add_product_to_basket()
    #page.solve_quiz_and_get_code()
    #time.sleep(20)
    #page.should_be_product_name()
    #page.should_be_product_price()
#    page.should_be_success_message()

#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_product_to_basket()
#    page.should_not_be_success_message()

#def test_guest_cant_see_success_message(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.should_not_be_success_message()

#def test_message_disappeared_after_adding_product_to_basket(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_product_to_basket()
#    page.should_be_disappeared()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()
    page.should_be_item_page()
    time.sleep(10)
    page.go_to_basket()
    page.should_be_basket_empty()
    page.should_be_message_empty_basket()