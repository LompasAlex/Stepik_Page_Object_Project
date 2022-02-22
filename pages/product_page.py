# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:19:34 2022

@author: lompa
"""

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def is_it_promo(self):
        assert "?promo=" in self.browser.current_url, "this is not promo page"
        
    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Basket button is not found"
        
    def go_to_add_to_basket_page(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()
        
    def is_book_name_correct(self):
        correct_book_name = self.browser.find_element(*ProductPageLocators.CORRECT_NAME).text
        added_book_name = self.browser.find_element(*ProductPageLocators.ADDED_NAME).text
        assert correct_book_name == added_book_name, "name of added to basket book does not match with selected"
        
    def is_price_book_correct(self):
        correct_book_price = self.browser.find_element(*ProductPageLocators.CORRECT_PRICE).text
        added_book_price = self.browser.find_element(*ProductPageLocators.ADDED_PRICE).text
        assert correct_book_price == added_book_price, "price of added to basket book does not match with selected"
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented, but should not be"
        
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),"Success message does not disappear"
        