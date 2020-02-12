from selenium import webdriver
import unittest
import pytest
import logging
from base.webdriverfactory import webdriverfactory
from base.webdriverfactory import webdriverfactory
from utilities.custom_logger import logger_file as cl
from pages.loginpage import loginpage


class logintest(unittest.TestCase):

    log = cl.custom_logger.custom_logger(logging.DEBUG)
    lp = loginpage()
    wb = webdriverfactory()
    init = wb.web_driver_factory.get_web_driver_instance()
    def successful_login(self):

        self.lp.login("aditi.padha@mindfiresolutions.com" , "mindfire@1")




