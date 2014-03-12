from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class RegistrationFb(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://pursuite.openlabs.us/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_registration_fb(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/account/signup/")
        driver.get("https://www.facebook.com/login.php?skip_api_login=1&api_key=597009120373156&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fredirect_uri%3Dhttp%253A%252F%252Fpursuite.openlabs.us%252Faccount%252Ffacebook%252Flogin%252Fcallback%252F%26state%3DP1Atgk9yBeVm%26scope%3Demail%26response_type%3Dcode%26client_id%3D597009120373156%26ret%3Dlogin&cancel_uri=http%3A%2F%2Fpursuite.openlabs.us%2Faccount%2Ffacebook%2Flogin%2Fcallback%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DP1Atgk9yBeVm%23_%3D_&display=page")
    
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
