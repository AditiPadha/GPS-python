import time
import traceback
import logging
import utilities.custom_logger.logger_file as cl


class utils(object):

    def verify_text_contains(self, actual_text, expected_text):
        self.log.info("ACtual text from the application web UI :: " + actual_text)
        self.log.info("Expected text from the application web UI :: " + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.log.info("### verification contains")
            return True
        else:
            self.log.info("### verification doesnt contains!!!")
            return False
