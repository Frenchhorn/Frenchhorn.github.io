import unittest, datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utils, config
from locators import * 
from scripts import *

driver = utils.browser()
utils.getIndex(driver)