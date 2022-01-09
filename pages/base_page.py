from selenium.common import exceptions
from selenium.webdriver.common.by import By



class BasePage(object):
	"""web page basic class"""
	def __init__(self, url, driver, timeout=5):
		'''
		input:
			url - page url
			driver - browser driver handler
			timeout - implicit timeout period
		'''
		self.url = url
		self.driver = driver
		self.driver.implicitly_wait(timeout)

	def open(self):
		self.driver.get(self.url)

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
