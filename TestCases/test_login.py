import sys

from PageObjects.loginPage import LoginPage
import time
from PageObjects.loginPage import LoginPage
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig
from Utilities.procs import compare_images


class Test_001_login:
    # set link to login page, username and password to use
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    # what driver to use, pass it from
    # setup
    # now get to the page, get its title and verify it


    def test_homePageTitle(self, setup):
        self.logger.info('--------Test_001, test_homePageTitle ----------')
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        print(f'Action title:{self.driver.title}')
        if self.driver.title == "Log in to gateway":
            self.logger.info('*** Test title page PASSED ***')
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot('../Screenshots/' + 'test_homePageTitleNew.png')
            self.driver.close()
            if not compare_images('../Screenshots/' + 'test_homePageTitleNew.png', '../Screenshots/' + 'test_homePageTitle.png'):
                self.logger.info('*** Test title page FAILED')
                assert False
            else:
                self.logger.info('*** Test title page Passed')
                assert True


    def test_login_page(self, setup):
        self.logger.info('--------Test_001, test_login ----------')
        self.driver = setup
        self.driver.delete_all_cookies()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        # here I get the login page
        self.lp.typeInUsername(self.username)
        self.lp.typeInPassword(self.password)
        self.lp.clickLogin()

        time.sleep(4)
        self.logger.info(f'---Test_001, test_login_page ---:{self.driver.title}')
        if self.driver.title == "Gateway":
            self.logger.info('*** Test_001, test_login_page -- PASSED ***')
            assert True
        else:
            self.logger.info('*** Test_001, test_login_page -- FAILED ***')
            assert False
        self.lp.clickLogout()
        self.driver.close()
