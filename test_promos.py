from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.custom_page_with_ny_promo import CustomNewYearPromoPage


product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(0, 10)]

 

@pytest.mark.parametrize('link', urls)
def test_promos(get_browser_driver, link):
	driver = get_browser_driver
	page = CustomNewYearPromoPage(link, driver)
	page.open()
	page.should_be_discount()
