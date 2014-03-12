from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class StudentJobSeekerWebpge(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://pursuite.openlabs.us/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_student_job_seeker_webpge(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/student-job-seeker/")
        self.assertEqual("Read", driver.find_element_by_css_selector("div.mid-box-flip > h1").text)
        self.assertEqual("Watch & Learn", driver.find_element_by_xpath("//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div/h1").text)
        self.assertEqual("Plan Your Career", driver.find_element_by_xpath("//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div/h1").text)
        self.assertEqual("Download", driver.find_element_by_xpath("//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[4]/div/h1").text)
    
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
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
