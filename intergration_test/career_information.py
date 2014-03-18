# -*- coding: utf-8 -*-
"""
    career_information

    Description goes here...

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import unittest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, \
     NoAlertPresentException
from base import Selenium2OnSauce

class Career(Selenium2OnSauce):

    def test_b_p_m(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/career-information/bpm/")

    def test_career_information_link(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-projects/analytics/")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Career Information"))

    def test_career_information_webpage(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/career-information/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))

    def test_e_r_d(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/career-information/erd/")

    def test_i_t_service(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/career-information/it-service/")

    def test_software_products(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/career-information/software-products/")

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
