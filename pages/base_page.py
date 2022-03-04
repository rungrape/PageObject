from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class BasePage(object):
	"""web page basic class"""
	def __init__(self, url, driver, timeout=3):
		'''
		input:
			url - page url
			driver - browser driver handler
			timeout - implicit timeout period
		'''
		self.url = url
		self.driver = driver
		self.driver.implicitly_wait(timeout)

	def get_elem(self, selector):
		return self.driver.find_element(By.CSS_SELECTOR, selector)

	def open(self):
		self.driver.get(self.url)

	def is_not_element_present(self, selector, timeout=4):
		try:
			WebDriverWait(self.driver, timeout, 1, exceptions.TimeoutException).until(\
				EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
		except exceptions.TimeoutException:
			return True
		return False

	def is_element_present(self, selector):
		try:
			self.driver.find_element(By.CSS_SELECTOR, selector)
		except exceptions.NoSuchElementException:
			return False
		return True

	def __del__(self):
		try:
			
			self.driver.close()
		except:
			pass

	def is_disappeared(self, selector, timeout=4):
		try:
			WebDriverWait(self.driver, timeout, 1, exceptions.TimeoutException).\
				until_not(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
		except exceptions.TimeoutException:
			return False

		return True

	def click_button(self, selector, timeout=4):
		add_to_basket_btn = self.get_elem(selector)
		add_to_basket_btn.click()

