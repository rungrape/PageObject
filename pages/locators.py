from selenium.webdriver.common.by import By


class MainPageLocators():
	LOGIN_LINK = "#login_link"

class LoginPageLocators():
	LOGIN_UNAME_INPUT = "#id_login-username"
	LOGIN_PASSW_INPUT = "#id_login-password"
	LOGIN_SUBMIT_BTN = "button[name='login_submit']"
	REG_UNAME_INPUT = "#id_login-username"
	REG_PASSW_INPUT = "#id_registration-email"
	REG_CONFIRM_PASSW_INPUT = "#id_registration-password2"
	REG_SUBMIT_BTN = "button[name='registration_submit']"

class CustomPageLocators():
    ADD_TO_BASKET_BTN = ".btn-add-to-basket"
    CUSTOM_LBL = "div.col-sm-6.product_main h1"
    SUCCESS_LBL = ".alert-success:nth-child(1) .alertinner > strong"
    BASKET_SUM = ".basket-mini.pull-right"
    CUSTOM_SUM = ".product_main .price_color"

class CustomNewYearPromoPageLocators(CustomPageLocators):
    pass
