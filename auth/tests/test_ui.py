from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def run_tests(view):
    browser = webdriver.Firefox()
    browser.quit()

class SeleniumTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(SeleniumTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SeleniumTestCase, self).tearDown()

    def test_login(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:8000/login/')
        username = selenium.find_element_by_id('user')
        password = selenium.find_element_by_id('pass')
        submit = selenium.find_element_by_name('login')
        username.send_keys('staff')
        password.send_keys('staff')

        submit.send_keys(Keys.RETURN)
        assert 'logout' in selenium.page_source