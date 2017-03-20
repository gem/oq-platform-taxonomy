#!/usr/bin/env python
import unittest
import os, sys, time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

from openquakeplatform.test import pla


class TaxonomyTest(unittest.TestCase):

    def content_test(self):

        pla.get('/taxonomy')

        letterlink = pla.xpath_finduniq(
            "//button[@data_letter='H']")
        letterlink.click()

        termlink = pla.xpath_finduniq(
            "//a[normalize-space(text())='Height of ground"
            " floor level above grade [HF]']")
        termlink.click()

        pla.wait_new_page(termlink, '/taxonomy/height-of-ground-floor-level-above'
                                    '-grade--hf', timeout=5)

        img = pla.xpath_finduniq(
            "//img[@alt='HF_diagram_-_1']")

        self.assertEqual(pla.driver.execute_script(
            "return arguments[0].complete && typeof"
            " arguments[0].naturalWidth"
            "  != \"undefined\" && arguments[0].naturalWidth > 0", img), True)

        intlink = pla.xpath_finduniq(
            "//a[@class='internal-link']")
        intlink.click()

        pla.xpath_finduniq(
            "//h2[normalize-space(text())='Ground floor']")

