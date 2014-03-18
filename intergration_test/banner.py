# -*- coding: utf-8 -*-
"""
    banner

    Description goes here...

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import unittest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, \
     NoAlertPresentException
from base import Selenium2OnSauce

class Banner(Selenium2OnSauce):

    def test_advanced_skills(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/foundation-advance-skills-development/advanced-skills/")
        self.assertTrue(self.is_element_present(By.ID, "wfmis"))

    def test_advanced_skills_epp(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/ssc-nasscom-training-programs/software-products/advanced-skills/")

    def test_advanced_skills_erd(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/ssc-nasscom-training-programs/erd/advanced-skills/")

    def test_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/ssc-nasscom-training-programs/bpm/")

    def test_central_overnment(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/research/government-research/central-government/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[4]/div"))

    def test_company_research(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/research/company-research/")

    def test_company_training_provider(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/company-training-programs/")

    def test_courseware(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/foundation-advance-skills-development/foundation-skills/courseware/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div"))

    def test_developing_tomorrow(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/")

    def test_download(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/foundation-advance-skills-development/foundation-skills/courseware/download/")

    def test_epp(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/ssc-nasscom-training-programs/erd/foundation-skills/epp/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))

    def test_erd(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/ssc-nasscom-training-programs/erd/")

    def test_event(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/event-workforce-enablement/")

    def test_executive_summary(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/foundation-advance-skills-development/foundation-skills/courseware/read-only/executive-summary/")

    def test_foundation_advance_skills_devlopment(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/foundation-advance-skills-development/")

    def test_foundation_convocation_banner(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.XPATH, "(//a[contains(text(),'Know More')])[3]"))
        driver.get("http://pursuite.openlabs.us/about-us/ssc-nasscom/vision-mission/")

    def test_foundation_skills_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/ssc-nasscom-training-programs/bpm/foundation-skills/")

    def test_foundation_skills_ed(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/ssc-nasscom-training-programs/erd/foundation-skills/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))

    def test_foundation_skills_epp(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/ssc-nasscom-training-programs/software-products/foundation-skills/")

    def test_full_course(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/foundation-advance-skills-development/foundation-skills/courseware/read-only/full-course/")

    def test_gbfs_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/ssc-nasscom-training-programs/bpm/foundation-skills/gbfs/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.filetitle"))

    def test_government(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/research/government-research/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))

    def test_government_research(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/research/government-research/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div"))

    def test_government_training_program(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/government-training-programs/")

    def test_healp_you_choose(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Know More"))

    def test_ict_academy_tamilnadu(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/private-sector-training-programs/ict-academy-tamilnadu/")

    def test_il_fs(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resougvrces/private-sector-training-programs/ilfs/")

    def test_implementation_cycle_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/ssc-nasscom-training-programs/bpm/foundation-skills/gbfs/implementation-cycle/")

    def test_interactive_tools(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/interactive-tools/")

    def test_it_initiative(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))

    def test_it_ites(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/it-ites-initiativesprograms/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[7]/div"))

    def test_listining_of_programs(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/event-workforce-enablement/listing-programs/")

    def test_nasscom_research(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/research/nasscom-research/")

    def test_niit(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/private-sector-training-programs/niit/")

    def test_obf_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/ssc-nasscom-training-programs/bpm/foundation-skills/gbfs/outcome-based-framework-gbfs/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.filetitle"))

    def test_other_bodies_government(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/government-training-programs/other-bodies/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))

    def test_other_bodies(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/research/government-research/other-bodies/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[4]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[5]/div"))

    def test_other_publication(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/foundation-advance-skills-development/foundation-skills/courseware/other-publication/")

    def test_policy_development(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/policy-development/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[4]/div"))

    def test_private_sector_training_programs(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/private-sector-training-programs/")

    def test_program_registration(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/event-workforce-enablement/program-registration/")

    def test_promotion_marketing(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/promotion-marketing/")

    def test_read_only(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/foundation-advance-skills-development/foundation-skills/courseware/read-only/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))

    def test_research(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/research/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))

    def test_skills_academy(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/private-sector-training-programs/skills-academy/")

    def test_software_products(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/ssc-nasscom-training-programs/software-products/")

    def test_ssc_training_programs(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/ssc-nasscom-training-programs/")

    def test_state_government(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/research/government-research/state-government/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[4]/div"))

    def test_talent_sprint(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/private-sector-training-programs/talent-sprint/")

    def test_training_materials(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/training-materials/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div"))

    def test_training_that_helps_you(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.XPATH, "(//a[contains(text(),'Know More')])[2]"))

    def test_training_tools(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/developing-tomorrows-workforce-today/training-programs-tools-resources/training-tools/")

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
