# -*- coding: utf-8 -*-
"""

    integration_test.test_case

    Base class for tests which optionally runs code on saucelabs

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: see LICENSE for more details.
"""
import os
import unittest

from selenium import webdriver


class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        if 'SAUCE_EXECUTOR' in os.environ:
            desired_capabilities = getattr(
                webdriver.DesiredCapabilities,
                os.environ.get('SAUSCE_DRIVER', 'FIREFOX')
            )
            desired_capabilities['platform'] = os.environ.get(
                "SAUCE_PLATFORM",
                "Windows 7"
            )
            desired_capabilities['version'] = os.environ.get(
                'SAUCE_VERSION', "27"
            )
            desired_capabilities['name'] = 'Testing pursuite at Sauce'

            self.driver = webdriver.Remote(
                desired_capabilities=desired_capabilities,
                command_executor=os.environ['SAUCE_EXECUTOR']
            )
        else:
            self.driver = webdriver.Firefox()

        self.base_url = "http://pursuite.openlabs.us"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.implicitly_wait(30)

    def tearDown(self):
        if 'SAUCE_EXECUTOR' in os.environ:
            print(
                "Link to your job:"
                "https://saucelabs.com/jobs/%s" % self.driver.session_id
            )
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
