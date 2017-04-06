from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest, datetime

BROWSER = 'chrome'
ENV = 'localhost'
RUN = 'all'
LOG_FILE = 'log_file.txt'

def browser(browserName):
    if browserName == 'chrome':
        return webdriver.Chrome(executable_path=r'C:\Users\qinpan.zhao\Desktop\phantomjs-2.1.1-windows\bin\chromedriver.exe')
    elif browserName == 'firefox':
        return webdriver.Firefox(executable_path=r'C:\Users\qinpan.zhao\Desktop\phantomjs-2.1.1-windows\bin\geckodriver.exe')
    elif browserName == 'ie':
        return webdriver.Ie(executable_path=r'C:\Users\qinpan.zhao\Desktop\phantomjs-2.1.1-windows\bin\IEDriverServer.exe')

class YunzhidaoIndex(unittest.TestCase):

    def setUp(self):
        self.driver = browser(BROWSER)
        if ENV == 'localhost':
            self.driver.get('http://localhost:4502/content/china/accl/solr/index.html')
            username = self.driver.find_element_by_id("username")
            username.send_keys("admin")
            password = self.driver.find_element_by_id("password")
            password.send_keys('admin')
            password.send_keys(Keys.RETURN)
        elif ENV == 'dev':
            self.driver.get('http://10.143.170.100:4503/content/china/accl/solr/index.html')

    def tearDown(self):
        self.driver.close()

    def test_search_click(self):
        driver = self.driver
        keyword = driver.find_element_by_xpath('//*[@id="autocomplete"]')
        keyword.send_keys('安利')
        submit = driver.find_element_by_xpath('//*[@id="searchFrom"]/div[2]/div/a')
        submit.click()

    def test_search_enter(self):
        driver = self.driver
        keyword = driver.find_element_by_xpath('//*[@id="autocomplete"]')
        keyword.send_keys('安利')
        submit = driver.find_element_by_xpath('//*[@id="searchFrom"]/div[2]/div/a')
        submit.send_keys(Keys.ENTER)

    def test_click_nutrilite(self):
        driver = self.driver
        nutrilite = driver.find_element_by_xpath('//*[@id="news-panel"]/ul/li[1]/a/img')
        nutrilite.click()
 
if __name__ == "__main__":
    with open(LOG_FILE, 'a') as f:
        f.write('\n**********************************************************************\n')
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        f.write('\n**********************************************************************\n')
        if RUN == 'all':
            runner = unittest.TextTestRunner(stream=f, verbosity=2)
            unittest.main(testRunner=runner)
        elif RUN != '':
            suite = unittest.TestSuite()
            suite.addTest(YunzhidaoIndex(RUN))
            runner = unittest.TextTestRunner(stream=f, verbosity=2)
            runner.run(suite)
        else:
            print("Don't run.")