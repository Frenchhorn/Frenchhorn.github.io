import unittest
from selenium import webdriver

driver  = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.ANDROID)
driver.get("https://www.baidu.com")
