# -*- coding: utf-8 -*-
"""
    search

    Description goes here...

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import unittest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, \
     NoAlertPresentException
from base import Selenium2OnSauce

class DeveloperSearchPagination(Selenium2OnSauce):

    def test_developer_search_pagination(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/search/?q=Developer")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Prev"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "1"))

    def test_search_developer(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/about-us/nasscom/")
        self.assertTrue(self.is_element_present(By.NAME, "q"))
        driver.get("http://pursuite.openlabs.us/search/?q=Developer")

    def test_search_governing_council(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/search/?q=Engineer+Trainee")
        self.assertTrue(self.is_element_present(By.NAME, "q"))
        driver.get("http://pursuite.openlabs.us/search/?q=Governing+Council")

    def test_search_engineer_trainee(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/about-us/nasscom/")
        self.assertTrue(self.is_element_present(By.NAME, "q"))
        driver.get("http://pursuite.openlabs.us/search/?q=Engineer+Trainee")

    def test_search_technical_writer(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/about-us/nasscom/")
        self.assertTrue(self.is_element_present(By.NAME, "q"))

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
