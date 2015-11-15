from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from functions.base_methods import BaseMethods


class GooglePage(BaseMethods):
    keyboard_id = 'gs_ok0'

    def __init__(self, driver):
        self.driver = driver
        """:type : WebDriver"""

# input text method
    def input_text(self, element, value):
        by = By.ID
        try:
            self.driver.find_element(by, element).clear()
            self.driver.find_element(by, element).send_keys(value)
        except NoSuchElementException:
            return print(element + ' nie istnieje')

# open keyboard method
    def open_keyboard(self):
        try:
            self.driver.find_element_by_id(self.keyboard_id).click()
        except NoSuchElementException:
            print ("Ikona klawiatury nie została znaleziona")