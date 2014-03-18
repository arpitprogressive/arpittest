import unittest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, \
     NoAlertPresentException
from base import Selenium2OnSauce


class AboutUs(Selenium2OnSauce):

    def test_about_us(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/about-us/")

    def test_central_government(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/development-initiatives/youth-program/government-initiative/central-government/")

    def test_committes_workforce_devlopment(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/development-initiatives/education-training/committees-workforce-development/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))

    def test_company_initiative(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/development-initiatives/youth-program/company-initiative/")

    def test_company_reports(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/research-reports/reports/company-reports/")

    def test_company_white_papers(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/research-reports/white-papers/company-whitepapers/")

    def test_coursera(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/development-initiatives/education-training/development-moocs/coursera/")

    def test_courseware(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/development-initiatives/education-training/fsit/foundation-skills/courseware/")

    def test_e_p_p(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/development-initiatives/education-training/epp/")

    def test_n_a_c_tech(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/development-initiatives/education-training/nac-tech/")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException:
            return False
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
        finally:
            self.accept_next_alert = True


if __name__ == "__main__":
    unittest.main()
