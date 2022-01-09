from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_guest_can_go_to_login_page(get_browser_driver):
	driver = get_browser_driver
	# --
	link = "http://selenium1py.pythonanywhere.com/"
	driver.get(link)
	login_link = driver.find_element_by_css_selector("#login_link")
	login_link.click()
