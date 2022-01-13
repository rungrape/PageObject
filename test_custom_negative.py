#4.3, task 6
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.custom_page import CustomPage


def test_guest_cant_see_success_message_after_adding_product_to_basket(get_browser_driver):
	driver = get_browser_driver
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
	page = CustomPage(link, driver, 0)
	page.open()
	page.should_not_be_success_msg_after_add()

def test_guest_cant_see_success_message(get_browser_driver):
	driver = get_browser_driver
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
	page = CustomPage(link, driver)
	page.open()
	page.should_not_be_success_msg()

def test_message_disappeared_after_adding_product_to_basket(get_browser_driver):
	driver = get_browser_driver
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
	page = CustomPage(link, driver)
	page.open()
	page.should_be_disappeared_success_msg_after_add()


