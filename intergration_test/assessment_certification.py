# -*- coding: utf-8 -*-
"""
    assessment_certification

    Description goes here...

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import unittest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, \
     NoAlertPresentException
from base import Selenium2OnSauce

class AssessmentCertificationLink(Selenium2OnSauce):

    def test_assessment_certification_link(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-projects/research-and-reports/demand-supply-analysis/")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Assessment & Certification"))
        driver.get("http://pursuite.openlabs.us/ssc-article/assessment-certification/")

    def test_assessment_certification_webpage(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/assessment-certification/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div"))

    def test_job_recruitment_sites(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/assessment-certification/")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Read More"))

    def test_job_recruitment_sites_webpage(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/assessment-certification/job-recruitment-sites/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.span9.article > div.row-fluid > ul > li"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Monster"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Monster"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Shine"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Jobs Ahead"))

    def test_n_a_c_read_more(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/assessment-certification/")
        self.assertTrue(self.is_element_present(By.XPATH, "(//a[contains(text(),'Read More')])[2]"))

    def test_n_a_c_tech_read_more(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/assessment-certification/")
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "(//a[contains(text(),'Read More')])[3]"))

    def test_n_a_c_tech_webpage(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/assessment-certification/nac-tech/")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Read More"))

    def test_n_a_c_webpage(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/assessment-certification/nac/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.filetitle"))

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
