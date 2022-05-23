from selenium import webdriver
from selenium.webdriver.common import by


class LoginPage:
    # define page labels and buttons
    print("**** from LoginPage class")

    link_logout_linktest = "Logout"
    page_title = 'Your store. Login'
    logged_in_title = 'Your store. Login'

    # define page labels and buttons
    textbox_username_id = "//*[@id='username']"
    textbox_password_id = "//*[@id='password']"
    button_login_xpath ="//*[@id='kc-login']"

    logout_xpath = "//*[contains(@class, 'cursor ng-binding')]"

    # what driver to use
    def __init__(self, driver):
        print('2. LoginPage ---------')
        self.driver = driver

    # what username and password to use for that page
    def typeInUsername(self, username):
        self.driver.find_element_by_xpath(self.textbox_username_id).clear()
        self.driver.find_element_by_xpath(self.textbox_username_id).send_keys(username)

    def typeInPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_id).clear()
        self.driver.find_element_by_xpath(self.textbox_password_id).send_keys(password)

    # define actions, click to login and logout
    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.logout_xpath).click()








