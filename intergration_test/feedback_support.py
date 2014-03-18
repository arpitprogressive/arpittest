# -*- coding: utf-8 -*-
"""
    feedback_support

    Description goes here...

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import unittest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, \
     NoAlertPresentException
from base import Selenium2OnSauce

class FeedbackSupportDialogBox(Selenium2OnSauce):

    def test_feedback_support_dialog_box(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Feedback & Support\"]"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "button"))

    def test_feedback_support_side_button(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Feedback & Support\"]"))

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True


if __name__ == "__main__":
    unittest.main()
