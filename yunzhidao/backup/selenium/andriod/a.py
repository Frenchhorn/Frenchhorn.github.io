import unittest
from selenium import webdriver


class FindElementTest(unittest.TestCase):

    def setUp(self):
        desired_capabilities = {'aut': 'com.tencent.mtt:7.1.2.2880'}

        self.driver = webdriver.Remote(desired_capabilities=desired_capabilities)
        self.driver.implicitly_wait(30)
        driver.get('and-activity://com.tencent.mtt.StartActivity')

    def test_find_element_by_id(self):
        self.driver.get('and-activity://com.tencent.mtt.HomeScreenActivity')
        self.assertTrue("and-activity://HomeScreenActivity" in self.driver.current_url)
        my_text_field = self.driver.find_element_by_id('my_text_field')
        my_text_field.send_keys('Hello Selendroid')

        self.assertTrue('Hello Selendroid' in my_text_field.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
