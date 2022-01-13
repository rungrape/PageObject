from .base_page import BasePage
from .locators import CustomPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time
from re import findall

def parse_num(f):
	return findall(r"£\d+\.\d+", f)[0][1:]

class CustomPage(BasePage):

	def __init__(self, url, driver, timeout=3):
		'''
		fields:
			url - page url
			driver - browser driver object
			timeout - time period for implicitly_wait
			basket_sum_prev - current basket sum before custom add
			custom_sum - current page custom price
			expected_sum - basket sum after custom add
		'''
		super().__init__(url, driver, timeout)
		self.basket_sum_prev = 0
		self.custom_sum = 0
		self.expected_sum = 0

	def open(self):
		self.driver.get(self.url)
		self.basket_sum_prev = self.get_price_in_float(CustomPageLocators.BASKET_SUM)
		self.custom_sum = self.get_price_in_float(CustomPageLocators.CUSTOM_SUM)

	def get_price_in_float(self, selector):
		txt = self.get_elem(selector).text
		num = float(parse_num(txt))
		return num

	def should_be_add_to_basket_btn(self):
		# check button presence, basket sum and custom price
		assert self.is_element_present(CustomPageLocators.ADD_TO_BASKET_BTN), "Add to basket button is not presented"

	def should_be_correct_sum_and_success_msg(self):
		'''
		WARNING: "add to basket" has to be already clicked
		'''
		# check success messages
		custom_name = self.get_elem(CustomPageLocators.CUSTOM_LBL).text
		success_msg = self.get_elem(CustomPageLocators.SUCCESS_LBL).text
		assert (custom_name == success_msg)
		# check sums
		actual_sum = self.get_price_in_float(CustomPageLocators.BASKET_SUM)
		expected_sum = self.basket_sum_prev + self.custom_sum
		assert expected_sum == actual_sum

	def should_not_be_success_msg_after_add(self):
		self.should_be_add_to_basket_btn()
		self.click_button(CustomPageLocators.ADD_TO_BASKET_BTN)
		self.is_not_element_present(CustomPageLocators.SUCCESS_LBL)

	def should_not_be_success_msg(self):
		self.should_be_add_to_basket_btn()
		self.is_not_element_present(CustomPageLocators.SUCCESS_LBL)

	def should_be_disappeared_success_msg_after_add(self):
		self.should_be_add_to_basket_btn()
		self.click_button(CustomPageLocators.ADD_TO_BASKET_BTN)
		self.is_disappeared(CustomPageLocators.SUCCESS_LBL)


