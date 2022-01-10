from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()

	def should_be_login_url(self):
		assert "/accounts/login/" in self.driver.current_url

	def should_be_login_form(self):
		assert self.is_element_present(LoginPageLocators.LOGIN_UNAME_INPUT), "Login username input is not presented"
		assert self.is_element_present(LoginPageLocators.LOGIN_PASSW_INPUT), "Login password input is not presented"
		assert self.is_element_present(LoginPageLocators.LOGIN_SUBMIT_BTN), "Login submit button is not presented"


	def should_be_register_form(self):
		assert self.is_element_present(LoginPageLocators.REG_UNAME_INPUT), "Registration username input is not presented"
		assert self.is_element_present(LoginPageLocators.REG_PASSW_INPUT), "Registration password input is not presented"
		assert self.is_element_present(LoginPageLocators.REG_CONFIRM_PASSW_INPUT), "Registration confirmation password input is not presented"
		assert self.is_element_present(LoginPageLocators.REG_SUBMIT_BTN), "Registration submit button is not presented"
		assert True
