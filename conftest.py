import sys

from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    print('0. Fixture ---------')
    chrome_path = r'C:\\Users\\ABenhida\\PycharmProjects\\Drivers\\chromedriver_100.4896.exe'

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    if browser == 'Safari':
        driver = webdriver.Safari()
    elif browser == 'Chrome':
        driver = webdriver.Chrome()
    else:
        print('... got here')
        driver = webdriver.Chrome(chrome_path, options=options)
    return driver


def pytest_addoption(parser):  #this will return the option value from cli/hooks
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):     # this will return the browser value to the setup method
    return request.config.getoption('--browser')

'''
# hook for adding environment info to HTML report
def pytest_configure(config):
    print('$$$$$$$$$ being called from pytest configure ')
    config._metadata['Project Name'] = 'nope Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Ahmed'
  
# hook to delete/modify environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

'''