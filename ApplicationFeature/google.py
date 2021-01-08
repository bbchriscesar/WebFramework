from PageObjects import locators as ss
from Framework.WebDriverMethods import WebDM
from Framework.CommonFunctions import Common
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

xpath = By.XPATH
id = By.ID
css = By.CSS_SELECTOR
name = By.NAME
className = By.CLASS_NAME

class Settings(object):
    def __init__(self, driver):
        self.driver = driver
        self.wdm = WebDM(self.driver)
        self.com = Common()
        self.browserDetails = self.com.readJSONConfig()
        self.path = self.com.get_screenshot_dir()
        self.screens = self.browserDetails['screenshots']['main_screen'].split(",")

    def googleFeature(self):
        self.wdm.navigateToURL(ss.test_URL)
        self.wdm.findAndClick(xpath, ss.search_bar)
        self.driver.find_element(xpath, ss.search_bar).send_keys(ss.search_text, Keys.ENTER)
        sleep(2)