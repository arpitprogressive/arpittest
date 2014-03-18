# -*- coding: utf-8 -*-
"""
    lets_grow_together

    Description goes here...

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import unittest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, \
     NoAlertPresentException
from base import Selenium2OnSauce

class EventsAndWorkshops(Selenium2OnSauce):

    def test_events_and_workshops(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/lets-grow-work-together/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Read More"))

    def test_internship(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/lets-grow-work-together/")
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "(//a[contains(text(),'Read More')])[2]"))

    def test_internship_webpage(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/lets-grow-work-together/internship/")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Read More"))
        self.assertTrue(self.is_element_present(By.XPATH, "(//a[contains(text(),'Read More')])[2]"))

    def test_let_s_grow_together_link(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-projects/")
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div/div/ul/li[2]/span"))

    def test_lets_grow_and_work_together_webapge(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/lets-grow-work-together/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))

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
