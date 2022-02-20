# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 11:30:00 2022

@author: lompa
"""
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_site_contain_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_elements(By.CLASS_NAME,"btn-add-to-basket"),'basket button not found'

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    time.sleep(5)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
    