# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 20:48:55 2022

@author: lompa
"""

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self): 
        self.browser.get(self.url)