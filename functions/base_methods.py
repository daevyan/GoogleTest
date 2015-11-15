from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BaseMethods:
    def __init__(self, driver):
        self.driver = driver
        """:type : WebDriver"""

# click method
    def click_element(self, element):
        by = By.XPATH
        try:
            self.driver.find_element(by, element).click()
        except NoSuchElementException:
            return print(element + ' nie istnieje')
