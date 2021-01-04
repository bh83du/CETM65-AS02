from selenium import webdriver
import unittest
import time

class Test_Data_Page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    # User goes to Webpage and expects to see 'Knowledge Base' on the page.
    def test_home_page_rendered(self):
        self.driver.get('http://127.0.0.1:8000')
        self.assertIn("Knowledge Base", self.driver.title,  "Text does not match expected") 

    # User goes to About Webpage and expects to see 'Knowledge Base About' on the page.
    def test_about_page_rendered(self):
        self.driver.get('http://127.0.0.1:8000/about')
        self.assertIn("Knowledge Base - About", self.driver.title,  "Text does not match expected") 


if __name__ == "__main__":
    unittest.main()