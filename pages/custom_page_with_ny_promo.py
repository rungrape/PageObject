from .base_page import BasePage
from .locators import CustomNewYearPromoLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time
from re import findall

def parse_num(f):
	return findall(r"£\d+\.\d+", f)[0][1:]

class CustomNewYearPromoPage(BasePage):

	def __init__(self, url, driver, timeout=3):
		super().__init__(url, driver, timeout)
		self.expected_sum = 0

	def get_price_in_float(self, selector):
		txt = self.get_elem(selector).text
		num = float(parse_num(txt))
		return num

	def solve_quiz_and_get_code(self):
		alert = self.driver.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.driver.switch_to.alert
			alert_text = alert.text
			print(f"Your code: {alert_text}")
			time.sleep(5)
			alert.accept()
			return True
		except NoAlertPresentException:
			print("No second alert presented")
			return True

	def should_be_discount(self):
		#self.should_be_promo_param()
		self.should_be_add_to_basket_btn()
		self.should_be_quiz_code()
		self.should_be_correct_sum_and_success_msg()

	def should_be_promo_param(self):
		assert "?promo=newYear" in self.driver.current_url

	def should_be_add_to_basket_btn(self):
		# check button presence, basket sum and custom price
		assert self.is_element_present(CustomNewYearPromoLocators.ADD_TO_BASKET_BTN), "Add to basket button is not presented"
		basket_sum_prev = self.get_price_in_float(CustomNewYearPromoLocators.BASKET_SUM)
		custom_sum = self.get_price_in_float(CustomNewYearPromoLocators.CUSTOM_SUM)
		self.expected_sum = basket_sum_prev + custom_sum
		# click "Add to basket" button
		add_to_basket_btn = self.get_elem(CustomNewYearPromoLocators.ADD_TO_BASKET_BTN)
		add_to_basket_btn.click()

	def should_be_quiz_code(self):
		assert self.solve_quiz_and_get_code()

	def should_be_correct_sum_and_success_msg(self):
		# check success messages
		custom_name = self.get_elem(CustomNewYearPromoLocators.CUSTOM_LBL).text
		success_msg = self.get_elem(CustomNewYearPromoLocators.SUCCESS_LBL).text
		assert (custom_name == success_msg)
		# check prices
		basket_sum_curr = self.get_price_in_float(CustomNewYearPromoLocators.BASKET_SUM)
		assert basket_sum_curr == self.expected_sum
