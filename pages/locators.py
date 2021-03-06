from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_PAGE = (By.CSS_SELECTOR, ".btn-group")
    ITEM_PAGE = (By.CSS_SELECTOR, ".image_container")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.NAME, "registration_submit")
    
class ProductPageLocators():
    ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR,".col-sm-6.product_main .price_color")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR,"#messages>div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")


class BasketPageLocators():
    BASKET_CATALOG = (By.CSS_SELECTOR, ".basket-items")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")


