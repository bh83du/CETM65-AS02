from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

DELAY = 3

class Test_Home_Page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000')


    def tearDown(self):
        self.driver.close()
    
    # User hears of Knowledgebase web application, and navigates to the URL.
    # 
    # User expects to see links to Articles, Login and Sign-Up pages.
    def test_home_page_rendered(self):        
        self.assertIn("ELCSS Knowledge Base", self.driver.title,  "Text does not match expected")
        self.driver.find_element_by_link_text("Articles")
        self.driver.find_element_by_link_text("Login")
        self.driver.find_element_by_link_text("Sign Up Here")

    # User expects to be able to search the Knowledgebase from the Navbar without logging in.
    def test_navbar_search_available_without_login(self):
        search = self.driver.find_element_by_name("q")
        search.send_keys("books")
        search.send_keys(Keys.ENTER)
        pagetitle_nav = self.driver.find_element_by_css_selector("h1")
        articletitle_nav = self.driver.find_element_by_css_selector("h2")
        self.assertEqual(pagetitle_nav.text, "Search Results")
        self.assertEqual(articletitle_nav.text, "Audio Books")

    # User expects to be able to search from the Home Page Search Bar without logging in.
    def test_homepage_search_available_without_login(self):
        searchbar = self.driver.find_element_by_css_selector("div > input")
        submit = self.driver.find_element_by_css_selector("div > input")
        searchbar.send_keys("books")
        submit.click()

    # Existing User exists to be be able to select Login and enter Username and Password to Login
    # After Login user is returned to Home Page
    def test_existing_user_login(self):
        self.driver.find_element_by_link_text("Login").click()
        time.sleep(DELAY)
        username = self.driver.find_element_by_id("id_username")
        password = self.driver.find_element_by_id("id_password")
        login = self.driver.find_element_by_css_selector(".form-group > .btn")
        username.clear()
        password.clear()
        username.send_keys("bh83du")
        password.send_keys("Testing321")
        login.click()
        time.sleep(DELAY)
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/")

    # Existing User logs out of the Application
    # On logout user is redirected to the Logout page
    def test_existing_user_logout(self):
        self.driver.find_element_by_link_text("Login").click()
        time.sleep(DELAY)
        username = self.driver.find_element_by_id("id_username")
        password = self.driver.find_element_by_id("id_password")
        login = self.driver.find_element_by_css_selector(".form-group > .btn")
        username.clear()
        password.clear()
        username.send_keys("bh83du")
        password.send_keys("Testing321")
        login.click()
        time.sleep(DELAY)
        self.driver.find_element_by_link_text("Logout").click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/logout/")

    # New User is able to sign up for an Account.
    def test_new_user_signs_up_for_account(self):
        self.driver.find_element_by_link_text("Sign Up Here").click()
        time.sleep(DELAY)
        username = self.driver.find_element_by_id("id_username")
        firstname = self.driver.find_element_by_id("id_first_name")
        lastname = self.driver.find_element_by_id("id_last_name")
        email = self.driver.find_element_by_id("id_email")
        password1 = self.driver.find_element_by_id("id_password1")
        password2 = self.driver.find_element_by_id("id_password2")
        username.send_keys("testuser999")
        firstname.send_keys("Test")
        lastname.send_keys("User")
        email.send_keys("test.user@testcompany.co.uk")
        password1.send_keys("Testing321")
        password2.send_keys("Testing321")
        self.driver.find_element_by_css_selector(".form-group > .btn").click()
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/login/")
        time.sleep(DELAY)
        success = self.driver.find_element_by_css_selector(".alert")
        self.assertEqual(success.text, "Success! Account created for testuser999. Please login.")









if __name__ == "__main__":
    unittest.main()
