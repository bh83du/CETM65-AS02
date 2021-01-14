from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

DELAY = 3

class Test_Articles_Page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000')
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

    def tearDown(self):
        self.driver.close()

    # Logged In User is able to create a new article:
    def test_create_new_article(self):
        self.driver.find_element_by_link_text("Create Article").click()
        time.sleep(DELAY)
        art_title = self.driver.find_element_by_id("id_title")
        art_title.send_keys("Article for Testing")
        self.driver.find_element_by_id("id_category").click()
        art_cat = self.driver.find_element_by_id("id_category")
        art_cat.find_element_by_xpath("//option[. = 'Knowledge Transfer']").click()
        self.driver.find_element_by_id("id_area").click()
        art_area = self.driver.find_element_by_id("id_area")
        art_area.find_element_by_xpath("//option[. = 'DevPortal']").click()
        self.driver.find_element_by_id("id_jiraid").click()
        self.driver.find_element_by_id("id_jiraid").send_keys("ELCSS-1999")
        ckeditor_frame = self.driver.find_element_by_class_name('cke_wysiwyg_frame')
        self.driver.switch_to.frame(ckeditor_frame)
        ck_editor_body = self.driver.find_element_by_tag_name("body")
        ck_editor_body.send_keys('This is a Test Article')
        self.driver.switch_to.default_content()
        self.driver.find_element_by_css_selector(".btn").click()

        # User is able to edit Article:
    def test_edit_article(self):
        self.driver.get('http://127.0.0.1:8000/user/bh83du/')
        self.driver.find_element_by_link_text("Article for Testing").click()
        time.sleep(DELAY)
        self.driver.find_element_by_link_text("Edit Article").click()
        art_title = self.driver.find_element_by_id("id_title")
        art_title.clear()
        art_title.send_keys("Article for Testing - Updated")
        self.driver.find_element_by_id("id_category").click()
        art_cat = self.driver.find_element_by_id("id_category")
        art_cat.find_element_by_xpath("//option[. = 'Testing']").click()
        self.driver.find_element_by_id("id_area").click()
        art_area = self.driver.find_element_by_id("id_area")
        art_area.find_element_by_xpath("//option[. = 'N/A']").click()
        self.driver.find_element_by_id("id_jiraid").click()
        self.driver.find_element_by_id("id_jiraid").send_keys("ELCSS-1999")
        ckeditor_frame = self.driver.find_element_by_class_name('cke_wysiwyg_frame')
        self.driver.switch_to.frame(ckeditor_frame)
        ck_editor_body = self.driver.find_element_by_tag_name("body")
        ck_editor_body.clear()
        ck_editor_body.send_keys('This is a Test Article - Updated')
        self.driver.switch_to.default_content()
        self.driver.find_element_by_css_selector(".btn").click()

        # User is able to delete an Article.  After Delete user is returned to full list of Articles
    def test_user_deletes_an_existing_article(self):
        self.driver.get('http://127.0.0.1:8000/user/bh83du/')
        self.driver.find_element_by_link_text("Article for Testing - Updated").click()
        time.sleep(DELAY)
        self.driver.find_element_by_link_text("Delete Article").click()
        time.sleep(DELAY)
        self.driver.find_element_by_css_selector(".btn-outline-danger").click()
        time.sleep(DELAY)
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:8000/articles/")



if __name__ == "__main__":
    unittest.main()