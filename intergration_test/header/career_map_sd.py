from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CareerMapSd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://pursuite.openlabs.us/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_career_map_sd(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/occupation/engineering-and-rd-software-development/?bc=%3Cli%3E%3Ca%20href%3D%22%2F%22%3EHome%3C%2Fa%3E%20%C2%BB%20%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22%2Fstakeholders%2Fgovernment%2F%22%3EGovernment%3C%2Fa%3E%20%C2%BB%20%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22%2Fstakeholders%2Fgovernment%2Fcareer-updates%2F%22%3ECareer%20Updates%3C%2Fa%3E%20%C2%BB%20%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22%2Fstakeholders%2Fgovernment%2Fcareer-updates%2Ferd%2F%22%3EEngineering%20Research%20and%20Development%3C%2Fa%3E%20%C2%BB%20%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fpursuite.openlabs.us%2Fstakeholders%2Fgovernment%2Fcareer-updates%2Ferd%2Fcareer-map-erd%2F%22%3ECareer%20Map%20of%20ERD%3C%2Fa%3E%20%C2%BB%20%3C%2Fli%3E")
    
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
