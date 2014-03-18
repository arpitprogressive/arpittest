# -*- coding: utf-8 -*-
"""
    footer

    Description goes here...

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import unittest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, \
     NoAlertPresentException
from base import Selenium2OnSauce

class Disclaimer(Selenium2OnSauce):

    def test_disclaimer(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Disclaimer"))
        driver.get(self.base_url + "pursuite.openlabs.us/policy-site-map/disclaimer/")

    def test_privacy_policy(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Privacy Policy"))
        driver.get(self.base_url + "pursuite.openlabs.us/policy-site-map/privacy-policy/")

    def test_sector_skills_council(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#block-block-13 > div.titlecontainer > h4.blocktitle"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "List of National Sector Skill Councils"))

    def test_security_policy(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Security Policy"))
        driver.get(self.base_url + "pursuite.openlabs.us/policy-site-map/security-policy/")

    def test_site_map(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Site Map"))
        driver.get(self.base_url + "pursuite.openlabs.us/policy-site-map/site-map/")

    def test_social_networking_facebook(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.icon-picon-facebook"))
        driver.get("https://www.facebook.com/NASSCOMOfficial")

    def test_social_networking_google_plus(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.icon-picon-gplus"))
        driver.get("https://plus.google.com/105749156768692050803/posts")

    def test_social_networking_linked_in(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.icon-picon-linkedin"))
        driver.get("http://www.linkedin.com/company/nasscom")

    def test_socail_networking_twitter(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.icon-picon-twitter"))
        driver.get("https://twitter.com/nasscom")

    def test_social_networking_youtube(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.icon-picon-youtube"))

    def test_terms_conditions(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Terms & Conditions"))
        driver.get("http://pursuite.openlabs.us/policy-site-map/terms-and-conditions/")

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
