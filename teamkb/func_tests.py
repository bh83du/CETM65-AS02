from selenium import webdriver
import unittest
import time

class Test_Data_Page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def tearDown(self):
        self.driver.close()
    
    # User hears of Knowledgebase web application, and navigates to the URL.
    def test_home_page_rendered(self):
        self.driver.get('http://127.0.0.1:8000')
        self.assertIn("ELCSS Knowledge Base", self.driver.title,  "Text does not match expected") 
        
    # User goes to About Webpage and expects to see 'Knowledge Base-About' in the page title.
    def test_about_page_rendered(self):
        self.driver.get('http://127.0.0.1:8000/about')
        self.assertIn("ELCSS Knowledge Base - About", self.driver.title,  "Text does not match expected") 
    
    #User wants to sign up to Knowledgebase Website.  Selects the Sign Up link
    def test_signup_page_rendered(self):
        self.driver.get('http://127.0.0.1:8000/signup')
        self.assertIn("ELCSS Knowledge Base - Sign Up", self.driver.title, "Text does not match expected")


if __name__ == "__main__":
    unittest.main()