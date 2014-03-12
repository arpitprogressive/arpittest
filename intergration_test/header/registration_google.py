from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class RegistrationGoogle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://pursuite.openlabs.us/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_registration_google(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/account/signup/")
        driver.get("https://accounts.google.com/AccountChooser?service=lso&continue=https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%3Fresponse_type%3Dcode%26scope%3Dhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%26redirect_uri%3Dhttp%3A%2F%2Fpursuite.openlabs.us%2Faccount%2Fgoogle%2Flogin%2Fcallback%2F%26state%3DQ2yEEGdLmN9f%26client_id%3D397663426216.apps.googleusercontent.com%26hl%3Den%26from_login%3D1%26as%3D6d29b2735b1831db&btmpl=authsub&hl=en")
    
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
