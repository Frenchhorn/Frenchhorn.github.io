from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import config

def browser(browserName=config.BROWSER):
    if browserName == 'chrome' or browserName == 'c':
        return webdriver.Chrome(executable_path=r'C:\Users\qinpan.zhao\Desktop\phantomjs-2.1.1-windows\bin\chromedriver.exe')
    elif browserName == 'firefox' or browserName == 'f':
        return webdriver.Firefox(executable_path=r'C:\Users\qinpan.zhao\Desktop\phantomjs-2.1.1-windows\bin\geckodriver.exe')
    elif browserName == 'ie' or browserName == 'i':
        return webdriver.Ie(executable_path=r'C:\Users\qinpan.zhao\Desktop\phantomjs-2.1.1-windows\bin\IEDriverServer.exe')
    else:
        return webdriver.PhantomJS(executable_path=r'C:\Users\qinpan.zhao\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')

def getIndex(driver, env=config.ENV):
    if env == 'local' or env == 'l':
        driver.get(config.LOCAL_DOMAIN + '/content/china/accl/solr/index.html')
        try:
            username = driver.find_element_by_id("username")
            username.send_keys(config.LOCAL_USER)
            password = driver.find_element_by_id("password")
            password.send_keys(config.LOCAL_PWD)
            password.send_keys(Keys.RETURN)
        except:
            pass
    elif env == 'dev' or env == 'd':
        driver.get(config.DEV_DOMAIN + '/content/china/accl/solr/index.html')
    elif env == 'qa' or env == 'q':
        driver.get(config.QA_DOMAIN + '/content/china/accl/solr/index.html')
    elif env == 'prod' or env == 'p':
        driver.get(config.PROD_DOMAIN + '/content/china/accl/solr/index.html')

def click(driver, element):
    driver.implicitly_wait(2)
    action = ActionChains(driver)
    action.move_to_element(element)
    action.click()
    action.perform()