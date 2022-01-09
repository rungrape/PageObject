from selenium import webdriver
import pytest
import time


def pytest_addoption(parser):
	'''
	test params parsing fixture
	'''
	parser.addoption('--language', action='store', default="en",
					 help="Choose language")


@pytest.fixture(scope='function')
def get_browser_driver(pytestconfig, autouse=True):
	'''
	teardown and setup fixture. launches
	Chrome with custom settings that is
	being set by cmd "language" param.
	'''
	lang = pytestconfig.getoption('language')
	# --
	options = webdriver.ChromeOptions()
	options.add_experimental_option('prefs', {'intl.accept_languages': lang})
	browser = webdriver.Chrome(options=options)
	# --
	yield browser
	browser.quit()
	# give user some time to lookup
	time.sleep(5)
