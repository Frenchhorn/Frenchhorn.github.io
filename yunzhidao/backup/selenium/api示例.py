from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pprint

print = pprint.pprint

driver = webdriver.Chrome(executable_path=r'C:\Users\qinpan.zhao\Desktop\phantomjs-2.1.1-windows\bin\chromedriver.exe')
#driver = webdriver.PhantomJS(executable_path=r'C:\Users\qinpan.zhao\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get("http://www.w3school.com.cn/")

#print('页面sourceCode:'+driver.page_source)
print('页面当前url:'+driver.current_url)
print('浏览器信息:')
print(driver.desired_capabilities)

'''
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print(elem.get_attribute('innerHTML'))
print(elem.get_attribute('outerHTML'))
print(elem.get_attribute('class'))
print(elem.value_of_css_property('height'))
'''
