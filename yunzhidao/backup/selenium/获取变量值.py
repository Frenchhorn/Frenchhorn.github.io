from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r'C:\Users\qinpan.zhao\Desktop\phantomjs-2.1.1-windows\bin\chromedriver.exe')   #2.25   supports v53-55
#driver = webdriver.PhantomJS(executable_path=r'C:\Users\qinpan.zhao\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')
#driver = webdriver.Firefox(executable_path=r'C:\Users\qinpan.zhao\Desktop\phantomjs-2.1.1-windows\bin\geckodriver.exe')
#driver = webdriver.Ie(executable_path=r'C:\Users\qinpan.zhao\Desktop\phantomjs-2.1.1-windows\bin\IEDriverServer.exe')
#driver = webdriver.Firefox()
driver.get('http://localhost:4502/content/china/accl/solr/index.html')
username = driver.find_element_by_id("username")
username.send_keys("admin")
password = driver.find_element_by_id("password")
password.send_keys('admin')
password.send_keys(Keys.RETURN)
a = 'return 123'
b = driver.execute_script(a)
print(b)