# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 20:49:15 2022

@author: lompa
"""

from .base_page import BasePage
# from .locators import MainPageLocators

class MainPage(BasePage): 
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)