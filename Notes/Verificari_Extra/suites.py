import unittest
from TA.curs10.alerts import Alerts
from TA.curs10.context_menu import Context_Menu
from TA.curs10.firefox_auth import Firefox
from TA.curs10.keys import Key
# Atentie, facem importul in functie de path-ul fisierului nostru
# in cazul meu, fisierul alerts.py in interiorul caruia am clasa Alerts se afla in folderul TA/curs10/, in cadrul proiectului curent...

"""
1. pip install html-testRunner
2. Din python packages => search for html-testRunner si instalam html-testrunner-1005D si html-testRunner
"""

import HtmlTestRunner


class TestSuite(unittest.TestCase):

    def test_suite(self):
        test_derulat = unittest.TestSuite()
        test_derulat.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
                              unittest.defaultTestLoader.loadTestsFromTestCase(Context_Menu),
                              unittest.defaultTestLoader.loadTestsFromTestCase(Firefox),
                              unittest.defaultTestLoader.loadTestsFromTestCase(Key)])

        runner = HtmlTestRunner.HTMLTestRunner(tested_by= 'Alexa Adela',
            title="Test Execution Report",
            report_name="AZI",

        )

        runner.run(test_derulat)
