from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
from utilities.custom_logger.logger_file import custom_logger as cl
import logging
import time
import os


class selenium_driver():
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locatortype):
        locator_type = locatortype.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "class":
            return By.CLASS_NAME
        else:
            self.log.info("Locator type" + locator_type + "not supported")

        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            byType = self.get_by_type(locator_type)
            element = self.driver.find_element(byType, locator)
            self.log.info("elemet found with locator:" + locator + "and locator type:" + locator_type)

        except:
            self.log.info("element not found with locator:" + locator + "and locator type is : " + locator_type)

        return element

    def enter_text(self , data, locator="" , locator_type="id"):
        element = None
        try:
            if locator: #This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("send data on teh element with locator:" + locator + " with locator type "+ locator_type)

        except:
            self.log.info("no element is found to send data ")

    def click_on_element(self, locator="", locator_type = "id"):
        element = None
        try:
            if locator:
                element = self.get_element(locator,locator_type="id")
            element.click()
            self.log.info("clicked on element with locator" + locator + "with locator_type" + locator_type)
        except:
            self.log.info("no element is found to be clicked with " + locator)

    def get_page_title(self, driver):
        return self.driver.title


