from .custom_page import CustomPage
from .locators import CustomNewYearPromoPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time
from re import findall

def parse_num(f):
	return findall(r"£\d+\.\d+", f)[0][1:]

class CustomNewYearPromoPage(CustomPage):

	def __init__(self, url, driver, timeout=3):
		super().__init__(url, driver, timeout)


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
		self.should_be_promo_param()
		self.should_be_add_to_basket_btn()
		self.click_button(CustomNewYearPromoPageLocators.ADD_TO_BASKET_BTN)
		self.should_be_quiz_code()
		self.should_be_correct_sum_and_success_msg()

	def should_be_promo_param(self):
		assert "?promo=newYear" in self.driver.current_url

	def should_be_quiz_code(self):
		assert self.solve_quiz_and_get_code()
