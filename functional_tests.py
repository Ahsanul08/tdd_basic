from selenium import webdriver
import unittest



class ToDoUserTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    def tearDown(self):
        self.browser.quit()

    def test_retrieve_title(self):
        self.browser.get('http://localhost:8000')
        assert 'To-Do' in self.browser.title
        self.fail("Finish the test")


if __name__ == '__main__':
    unittest.main(warnings='ignore')