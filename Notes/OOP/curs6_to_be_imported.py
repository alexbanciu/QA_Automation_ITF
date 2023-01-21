class TestCase1:
    def test_exe(self):
        print("Running testCase1")

    def runTwice(self):
        print("Run test again")


class TestCase2:
    def test_exe(self):
        print("Running testCase2")


class TestCase3:
    def __init__(self, name, summary):
        self.name = name
        self.summary = summary

    def get_name(self):
        return self.name

    def get_summary(self):
        return self.summary

    def test_exe(self):
        print("Running testCase3")

    def runTwice(self):
        print("Run test case 3 again")