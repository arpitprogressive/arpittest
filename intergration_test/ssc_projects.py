# -*- coding: utf-8 -*-
"""
    ssc_projects

    Description goes here...

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import unittest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, \
     NoAlertPresentException
from base import Selenium2OnSauce

class AnalysisOfSupplyChain(Selenium2OnSauce):

    def test_analysis_of_supply_chain(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-projects/research-and-reports/analysis-supply-chain-wrt-academic-outcomes/")

    def test_analytics(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-projects/analytics/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))

    def test_occupational_standards_webpage(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-projects/research-and-reports/occupational-standards/")

    def test_research_reports_webpage(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-projects/research-and-reports/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))

    def test_s_s_c_projects_webpage(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-projects/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "p > a"))

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
