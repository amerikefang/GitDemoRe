import unittest
from selenium import webdriver
import time

class GoogleTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def testPageTitle(self):
        self.browser.get('http://www.yahoo.com')
        self.assertIn('Yahoo', self.browser.title)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
