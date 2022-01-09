from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.main_page import MainPage



def test_guest_can_go_to_login_page(get_browser_driver):
	driver = get_browser_driver
	link = "http://selenium1py.pythonanywhere.com/"
	page = MainPage(link, driver)
	page.open()
	page.go_to_login_page()
