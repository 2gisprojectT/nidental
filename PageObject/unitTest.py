from unittest import TestCase
from selenium import webdriver
from page import Page
import unittest

class SeleniumWithPage(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.page.open("https://github.com/login")

    def testCorrectLogin(self):
        # self.page.setLogin("loginkuxDRjzq2015").setPassword("loginmbgDRxhf2015").input()
        self.page.login_form.login("loginkuxDRjzq2015", "loginmbgDRxhf2015")
        # self.assertEqual("@loginkuxDRjzq2015",self.page.getUserName())
        self.assertEqual("@loginkuxDRjzq2015",self.page.login_form.getUserName())
    def testIncorrectLogin(self):
        # self.page.setLogin("12345").setPassword("12345").input()
        self.page.login_form.login("12345", "12345")
        # self.assertEqual("https://github.com/session",self.page.getCurrentUrl())
        self.assertEqual("https://github.com/session",self.page.login_form.getCurrentUrl())

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()