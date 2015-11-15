import unittest
from selenium import webdriver
from functions.base_methods import BaseMethods
from pages.google_page import GooglePage


class GooglePageTest(unittest.TestCase):
    google = "https://www.google.pl/"
    search_bar = "lst-ib"
    lucky_find = "//*[@value='Szczęśliwy traf']"
    about_us = "//*[@id='fsl'/a[3]"
    keyboard_id = 'kbd'

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.google)
        self.driver.maximize_window()
        self.google_page = GooglePage(self.driver)

    def test_simple_search(self):
        self.google_page.input_text(self.search_bar, "pyrkon\n")
        self.driver.implicitly_wait(3)
        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://www.google.pl/#q=pyrkon")

    def test_is_keyboard_visible(self):
        self.google_page.open_keyboard()
        self.driver.implicitly_wait(3)
        self.assertTrue(self.driver.find_element_by_id(self.keyboard_id).is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
