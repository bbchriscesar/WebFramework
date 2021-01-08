from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as chains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

xpath = By.XPATH
id = By.ID
css = By.CSS_SELECTOR
name = By.NAME
className = By.CLASS_NAME

class WebDM(object):
    def __init__(self, driver):
        self.driver = driver

    def quit_driver(self):
        self.driver.quit()

    def navigateToURL(self, URL):
        self.driver.get(URL)
        sleep(2)

    def findAndClick(self, locator, value):
        self.driver.find_element(locator, value).click()
        sleep(2)