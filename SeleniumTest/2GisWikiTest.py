from unittest import TestCase
import unittest
from selenium import webdriver



class SeleniumTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://google.ru")

        self.driver = webdriver.Remote("http://localhost:9515",webdriver.DesiredCapabilities.CHROME)
        self.driver.get("https://google.ru")



    def test_search(self):

        search = self.driver.find_element_by_name("q")
        search.send_keys("2гис dbrb")
        search.submit()
        self.driver.implicitly_wait(10)
        link = self.driver.find_element_by_tag_name('i')
        link.click()
        self.driver.implicitly_wait(5)
        continue_link = self.driver.find_element_by_tag_name('h3').find_element_by_tag_name('a')
        self.driver.implicitly_wait(15)
        continue_link.click()
        self.driver.switch_to_window(self.driver.window_handles[-1])
        # title=self.driver.title
        head = self.driver.find_element_by_id("firstHeading")
        self.assertEqual('2ГИС', head.text)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()