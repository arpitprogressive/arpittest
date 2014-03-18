# -*- coding: utf-8 -*-
"""
    header

    Description goes here...

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import unittest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, \
     NoAlertPresentException
from base import Selenium2OnSauce


class AcademiaBpm(Selenium2OnSauce):

    def test_academia_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/bpm/foundation-skills/gbfs/implementation-cycle/academia-universities/")

    def test_academia(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/it-services/foundation-skills/fsit/implementation-cycle/academia-universities/")

    def test_advanced_skills_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/bpm/advanced-skills/")
        self.assertTrue(self.is_element_present(By.ID, "wfmis"))

    def test_advanced_skills(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/it-services/advanced-skills/")

    def test_advanced_skills_sp(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/software-products/advanced-skills/")
        self.assertTrue(self.is_element_present(By.ID, "wfmis"))

    def test_bpm_career_updates(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/bpm/")

    def test_bpm_industry(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/industry-where-are-we/career-information/bpm/")

    def test_bpm_industry_sub_sector(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/industry-sub-sector/bpm/")

    def test_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/company-training-programs/bpm/")

    def test_career_advice(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/student-job-seeker/read/job-profiles/")

    def test_career_map_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/bpm/career-map-bpm/")

    def test_career_map_erd_cu(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/erd/career-map-erd/")

    def test_career_map_erd(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/government/career-updates/erd/career-map-erd/")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Engineering Analysis"))

    def test_career_map_it(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/it-services/career-map-its/")

    def test_career_map(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/government/career-updates/it-service/career-map-its/")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Application Development"))

    def test_career_map_sd(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/occupation/engineering-and-rd-software-development/?bc=%3Cli%3E%3Ca%20href%3D%22%2F%22%3EHome%3C%2Fa%3E%20%C2%BB%20%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22%2Fstakeholders%2Fgovernment%2F%22%3EGovernment%3C%2Fa%3E%20%C2%BB%20%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22%2Fstakeholders%2Fgovernment%2Fcareer-updates%2F%22%3ECareer%20Updates%3C%2Fa%3E%20%C2%BB%20%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22%2Fstakeholders%2Fgovernment%2Fcareer-updates%2Ferd%2F%22%3EEngineering%20Research%20and%20Development%3C%2Fa%3E%20%C2%BB%20%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fpursuite.openlabs.us%2Fstakeholders%2Fgovernment%2Fcareer-updates%2Ferd%2Fcareer-map-erd%2F%22%3ECareer%20Map%20of%20ERD%3C%2Fa%3E%20%C2%BB%20%3C%2Fli%3E")

    def test_career_planning_study_bpm_cu(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/bpm/career-planning-study/")

    def test_career_planning_study_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/bpm/career-planning-study/")

    def test_career_planning_study_cu(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/software-products/career-planning-study/")

    def test_career_planning_study_erd_cu(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/erd/career-planning-study/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "p"))

    def test_career_planning_study_erd(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/government/career-updates/erd/career-planning-study/")

    def test_career_planning_study_itservices(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/it-services/career-planning-study/")

    def test_career_planning_study_sp_cu(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/software-products/career-planning-study/")

    def test_career_planning_study_sp(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/government/career-updates/software-products/career-planning-study/")

    def test_career_posters(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/student-job-seeker/read/career-posters/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Postrer1\"]"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Carrer Posters 2 LIMS\"]"))
        self.assertTrue(self.is_element_present(By.XPATH, "(//img[@alt='Postrer1'])[2]"))
        self.assertTrue(self.is_element_present(By.XPATH, "(//img[@alt='Carrer Posters 2 LIMS'])[2]"))

    def test_career_products_sp(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/government/career-updates/software-products/career-map-spd/")

    def test_career_updates_industry(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[4]/div"))

    def test_career_updates(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/")

    def test_career_videos(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/student-job-seeker/watch-learn/career-videos-youtube/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Career Videos\"]"))
        self.assertTrue(self.is_element_present(By.ID, "video-plugin-3457"))

    def test_central_government(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/government/central-government/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))

    def test_certifications(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/student-job-seeker/download/certifications/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.span9.article > div.row-fluid"))

    def test_company_training_programs(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/company-training-programs/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[4]/div"))

    def test_downloads(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-projects/capacity-building-and-development/efficacy-measures-assessments/nac/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.filetitle"))

    def test_epp(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/training-materials/epp/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.filetitle"))

    def test_erd_career_updates(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/erd/")

    def test_erd_government(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/government/career-updates/erd/")

    def test_erd_iss(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/industry-sub-sector/erd/")

    def test_erd(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/company-training-programs/erd/")

    def test_erd_scc_nascom_tp(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/erd/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))

    def test_font(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a.defaultFont"))

    def test_foundation_skills_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/bpm/foundation-skills/")

    def test_foundation_skills_erd(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/erd/foundation-skills/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))

    def test_foundation_skills(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/it-services/foundation-skills/")

    def test_foundation_skills_sp(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/software-products/foundation-skills/")

    def test_fsit(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/training-materials/fsit/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.filetitle"))

    def test_fsit_ssc_nasscom_tp(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/it-services/foundation-skills/fsit/")

    def test_gbfs(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/training-materials/gbfs/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.filetitle"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/p[7]"))

    def test_government_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/bpm/foundation-skills/gbfs/implementation-cycle/government/")

    def test_government(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/it-services/foundation-skills/fsit/implementation-cycle/government/")

    def test_implementation_cycle_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/bpm/foundation-skills/gbfs/implementation-cycle/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div"))

    def test_implementation_cycle_erd(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/erd/foundation-skills/epp/implementation-cycle/")

    def test_implementation_cycle(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/it-services/foundation-skills/fsit/implementation-cycle/")

    def test_industry_sub_sector(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/industry-sub-sector/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[4]/div"))

    def test_internship_info_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/bpm/internship-information/")

    def test_internship_info_career_update(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/it-services/internship-information/")

    def test_internship_info_itservices(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/it-services/career-planning-study/")

    def test_internship_info(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/it-services/internship-information/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "p"))

    def test_internship_info_sp_cu(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/software-products/internship-information/")

    def test_internship_info_sp(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/government/career-updates/software-products/internship-information/")

    def test_intership_info_erd(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/government/career-updates/erd/internship-information/")

    def test_iteractive_tools(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/interactive-tools/")

    def test_it_services_cu(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/it-services/")

    def test_it_services_iss(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/industry-sub-sector/it-services/")

    def test_it_services(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/company-training-programs/it-services/")

    def test_it_services_ssc_nasscom(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/it-services/")

    def test_job_profiles(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/student-job-seeker/read/job-profiles/")

    def test_key_ministries(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/government/central-government/key-ministries/")

    def test_language(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.WrapperWidth"))

    def test_login(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/account/login/")

    def test_nac(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-projects/capacity-building-and-development/efficacy-measures-assessments/nac/")

    def test_nac_tech(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-projects/capacity-building-and-development/efficacy-measures-assessments/nac-tech/")

    def test_nasscom_about_us(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/nasscom/")

    def test_obf_fsit_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/bpm/foundation-skills/gbfs/outcome-based-framework-gbfs/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.filetitle"))

    def test_obf_fsit_erd(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/erd/foundation-skills/epp/epp/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.filetitle"))

    def test_obf_fsit(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/it-services/foundation-skills/fsit/outcome-based-framework-fsit/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "p.plugin_file"))

    def test_obf(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-article/it-ites-initiative/foundation-advance-skills-development/foundation-skills/outcome-based-framework/gbfs/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "span.filetitle"))

    def test_occupational_standards(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/occupational-standard/SSC/N0201/")

    def test_other_minitries(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/government/central-government/other-ministries/")

    def test_plan_your_career(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-projects/career-path/")

    def test_qualifications_packs(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/ssc-projects/job-roles-and-qualification-packs/list-qualification-packs/")
        driver.get("http://pursuite.openlabs.us/qualification-pack/SSC/Q2601/")

    def test_read(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/student-job-seeker/read/")
        self.assertEqual("Career Posters", driver.find_element_by_css_selector("div.mid-box-flip > h1").text)
        self.assertEqual("Job Profiles", driver.find_element_by_xpath("//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div/h1").text)
        self.assertEqual("Career Advice", driver.find_element_by_xpath("//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div/h1").text)

    def test_registration_fb(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/account/signup/")
        driver.get("https://www.facebook.com/login.php?skip_api_login=1&api_key=597009120373156&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fredirect_uri%3Dhttp%253A%252F%252Fpursuite.openlabs.us%252Faccount%252Ffacebook%252Flogin%252Fcallback%252F%26state%3DP1Atgk9yBeVm%26scope%3Demail%26response_type%3Dcode%26client_id%3D597009120373156%26ret%3Dlogin&cancel_uri=http%3A%2F%2Fpursuite.openlabs.us%2Faccount%2Ffacebook%2Flogin%2Fcallback%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DP1Atgk9yBeVm%23_%3D_&display=page")

    def test_registration_google(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/account/signup/")
        driver.get("https://accounts.google.com/AccountChooser?service=lso&continue=https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%3Fresponse_type%3Dcode%26scope%3Dhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile%2Bhttps%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%26redirect_uri%3Dhttp%3A%2F%2Fpursuite.openlabs.us%2Faccount%2Fgoogle%2Flogin%2Fcallback%2F%26state%3DQ2yEEGdLmN9f%26client_id%3D397663426216.apps.googleusercontent.com%26hl%3Den%26from_login%3D1%26as%3D6d29b2735b1831db&btmpl=authsub&hl=en")

    def test_registration_linkedin(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/account/signup/")
        driver.get("https://www.linkedin.com/uas/oauth/authorize?oauth_token=75--abe5c628-75c4-4c7f-a1d5-a9b0fa8f030b&state=")

    def test_registration(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/account/signup/")

    def test_software_products_cu(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/career-updates/software-products/")

    def test_software_products_government(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/government/career-updates/software-products/")

    def test_software_products_iss(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/industry/industry-sub-sector/software-products/")

    def test_software_products(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/company-training-programs/software-products/")

    def test_software_products_ssc_nasscom(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/software-products/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))

    def test_ssc_nasscom_tp(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/")

    def test_stakeholder(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/student-job-seeker/read/career-advice/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Priyabala career Advice\"]"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"M S Raghunatha\"]"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Chinmay Career Advices\"]"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Narsingh Panigiri Career Advices\"]"))

    def test_state_government(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/government-training-programs/state-government/")

    def test_student_jobseeker(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/student-job-seeker/")
        self.assertEqual("Read", driver.find_element_by_css_selector("div.mid-box-flip > h1").text)
        self.assertEqual("Watch & Learn", driver.find_element_by_xpath("//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div/h1").text)
        self.assertEqual("Plan Your Career", driver.find_element_by_xpath("//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div/h1").text)
        self.assertEqual("Download", driver.find_element_by_xpath("//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[4]/div/h1").text)

    def test_student_job_seeker_webpge(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/student-job-seeker/")
        self.assertEqual("Read", driver.find_element_by_css_selector("div.mid-box-flip > h1").text)
        self.assertEqual("Watch & Learn", driver.find_element_by_xpath("//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div/h1").text)
        self.assertEqual("Plan Your Career", driver.find_element_by_xpath("//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div/h1").text)
        self.assertEqual("Download", driver.find_element_by_xpath("//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[4]/div/h1").text)

    def test_training_institute_bpm(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/bpm/foundation-skills/gbfs/implementation-cycle/training-institute/")

    def test_training_institute_itservices(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/it-services/foundation-skills/fsit/implementation-cycle/training-institute/")

    def test_training_institute(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/ssc-nasscom-training-programs/it-services/foundation-skills/fsit/implementation-cycle/training-institute/")

    def test_training_materials(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/training-materials/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div"))

    def test_training_provider(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/")

    def test_training_provider_webpage(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div"))

    def test_training_tools(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/training-provider/training-tools/")

    def test_watch_learn(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/student-job-seeker/watch-learn/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.mid-box-flip > h1"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[2]/div/h1"))
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='contentAndSidebars']/div/div[2]/div[2]/div/div/div[3]/div/h1"))

    def test_who_who_it(self):
        driver = self.driver
        driver.get("http://pursuite.openlabs.us/stakeholders/student-job-seeker/watch-learn/whos-who/")
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.span9.article > div.row-fluid"))
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "img[alt=\"whos who\"]"))

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
