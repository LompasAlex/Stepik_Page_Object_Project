# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 20:49:15 2022

@author: lompa
"""

from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()