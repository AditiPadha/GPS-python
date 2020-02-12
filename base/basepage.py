from base.selenium_driver import selenium_driver
from traceback import print_stack
from utilities.utils import  utils

class basepage(selenium_driver):

    def __init__(self,driver):
        super(basepage, self).__init__(driver)
        self.driver = driver
        self.util = utils()

    def verify_page_title(self, title_to_verfify):
        try:
            actual_text = self.get_page_title()
            actual_title = self.verify_page_title (actual_text, title_to_verfify)

        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False
