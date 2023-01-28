import unittest
from Alerts import Alerts
from Keys import Key
from Context_menu import Context_Menu
from Firefox import Firefox
from Tema9 import Login

#din fisier se importa clasa
import HTMLTestRunner

class TestSuite(unittest.TestCase):
    def test_suite1(self):
        test_derulat = unittest.TestSuite()
        test_derulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Alerts))
        test_derulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Key))
        test_derulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Context_Menu))
        test_derulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Firefox))
        test_derulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Login))


        runner = HTMLTestRunner.HTMLTestRunner(combine_reports=True, report_title= "Suites_Tema_10", report_name="Suites tema 10")
        runner.run(test_derulat)