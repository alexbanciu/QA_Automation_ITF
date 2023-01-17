import unittest
from Alerts import Alerts
#din fisier se importa clasa
import HTMLTestRunner

class TestSuite(unittest.TestCase):
    def test_suite(self):
        test_derulat = unittest.TestSuite()
        test_derulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Alerts))
        runner = HTMLTestRunner.HTMLTestRunner(combine_reports=True, report_title= "My first report", report_name="My first report Name")
        runner.run(test_derulat)