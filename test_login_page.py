from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.login_page import LoginPage


def test_guest_can_do_login(get_browser_driver):
	driver = get_browser_driver
	link = "http://selenium1py.pythonanywhere.com/accounts/login/"
	page = LoginPage(link, driver)
	page.open()
	page.should_be_login_page()
