from selenium import webdriver
import unittest
import time

class Test_Data_Page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    # User goes to Webpage and expects to see Django in the title
    def test_data_page_rendered(self):
        self.driver.get('http://127.0.0.1:8000')
        self.assertIn("Django", self.driver.title,  "Webpage Name does not match expected") 


if __name__ == "__main__":
    unittest.main()