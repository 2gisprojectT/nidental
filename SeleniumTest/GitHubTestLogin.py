from unittest import TestCase
import unittest
from selenium import webdriver


class SeleniumTest(TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()
        # self.driver.get("https://github.com/login")

        self.driver = webdriver.Remote("http://localhost:9515",webdriver.DesiredCapabilities.CHROME)
        self.driver.get("https://github.com/login")

# loginkuxDRjzq2015
# loginmbgDRxhf2015

    def test_search(self):
        login=self.driver.find_element_by_id("login_field")
        # login.click()
        login.send_keys("loginkuxDRjzq2015")

        password=self.driver.find_element_by_id("password")
        password.send_keys("loginmbgDRxhf2015")

        sumbit=self.driver.find_element_by_name("commit")
        sumbit.click()

        avatar = self.driver.find_element_by_class_name("avatar")
        name = avatar.get_attribute("alt")
        # avatar.click()
        self.assertEqual("@loginkuxDRjzq2015",name)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()