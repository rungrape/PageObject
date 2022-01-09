
class BasePage(object):
	"""web page basic class"""
	def __init__(self, url, driver):
		'''
		input:
			url - page url
			driver - browser driver handler
		'''
		super(BasePage, self).__init__()
		self.url = url
		self.driver = driver

	def open(self):
		self.driver.get(self.url)

	def __del__(self):
		try:
			self.driver.close()
		except:
			pass
