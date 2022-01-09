from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
	"""main page basic class"""
	def go_to_login_page(self):
		login_lnk = self.driver.find_element(By.CSS_SELECTOR, "#login_link")
		login_lnk.click() 
