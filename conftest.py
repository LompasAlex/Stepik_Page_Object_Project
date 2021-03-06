# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 11:29:25 2022

@author: lompa
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages':
                                              browser_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()