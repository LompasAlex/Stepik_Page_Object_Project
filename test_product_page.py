# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:18:14 2022

@author: lompa
"""

from .pages.product_page import ProductPage
import pytest
import time


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

# def test_guest_can_add_product_to_basket(browser):
#     page = ProductPage(browser,link)
#     page.open()
#     page.is_it_promo()
#     page.should_be_basket_button()
#     page.go_to_add_to_basket_page()
#     page.solve_quiz_and_get_code()
#     # time.sleep(100)
    
#     # page.should_not_be_success_message()
#     page.should_disappear_success_message()
    
#     # page.is_book_name_correct()
#     # page.is_price_book_correct()

# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser,link)
#     page.open()
#     page.should_be_basket_button()
#     page.go_to_add_to_basket_page()
#     page.solve_quiz_and_get_code()
#     page.should_not_be_success_message()

  
# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser,link)
#     page.open()    
#     page.should_not_be_success_message()

# @pytest.mark.xfail    
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser,link)
#     page.open()
#     page.should_be_basket_button()
#     page.go_to_add_to_basket_page()
#     page.solve_quiz_and_get_code()
#     page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


