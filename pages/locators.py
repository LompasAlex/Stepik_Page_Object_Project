# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 19:33:34 2022

@author: lompa
"""

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    CORRECT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADDED_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    CORRECT_PRICE = (By.CSS_SELECTOR, ".product_main p")
    ADDED_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner p strong")
    