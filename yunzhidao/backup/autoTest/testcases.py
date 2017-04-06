import unittest, datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utils, config
from locators import * 
from scripts import *

class YunzhidaoIndex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = utils.browser()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        utils.getIndex(self.driver)

    def tearDown(self):
        pass

    def test_search_button_all(self):
        
        search_bar = self.driver.find_element(*Landing.SEARCH_BAR)
        utils.click(self.driver, search_bar)
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located(SearchInput.SEARCH_INPUT), 'Cannot enter into searchInput Page')
        searchType = self.driver.execute_script(SearchInputScript.SEARCHTYPE)
        self.assertEqual(searchType, 'all')
 
    def test_search_button_video(self):
        video_button = self.driver.find_element(*Landing.SEARCHTYPE_VIDEO)
        utils.click(self.driver, video_button)
        video_button_input = self.driver.find_element(*Landing.SEARCHTYPE_VIDEO_INPUT)
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_selected(video_button_input), 'Video button is not selected')
        search_bar = self.driver.find_element(*Landing.SEARCH_BAR)
        utils.click(self.driver, search_bar)
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located(SearchInput.SEARCH_INPUT), 'Cannot enter into searchInput Page')
        searchType = self.driver.execute_script(SearchInputScript.SEARCHTYPE)
        self.assertEqual(searchType, 'video')

    def test_search_button_image(self):
        image_button = self.driver.find_element(*Landing.SEARCHTYPE_IMAGE)
        utils.click(self.driver, image_button)
        image_button_input = self.driver.find_element(*Landing.SEARCHTYPE_IMAGE_INPUT)
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_selected(image_button_input), 'Image button is not selected')
        search_bar = self.driver.find_element(*Landing.SEARCH_BAR)
        utils.click(self.driver, search_bar)
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located(SearchInput.SEARCH_INPUT), 'Cannot enter into searchInput Page')
        searchType = self.driver.execute_script(SearchInputScript.SEARCHTYPE)
        self.assertEqual(searchType, 'image')
 
    def test_category_news(self):
        news_content = self.driver.find_element(*Landing.CATEGORY_NEWS_CONTENT)
        self.assertTrue(news_content.is_displayed(), 'News category content disappear')
        first_item = self.driver.find_element(*Landing.getCategory(1))
        item_name = self.driver.execute_script(IndexScript.getCategoryName(1))
        utils.click(self.driver, first_item)
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located(Category.CATEGORY), 'Cannot enter into category Page')
        category_name = self.driver.execute_script(CategoryScript.CATEGORY_TITLE)
        self.assertTrue(item_name == category_name, 'Category title not true')
 
    def test_category_video(self):
        category_button = self.driver.find_element(*Landing.CATEGORY_VIDEO)
        utils.click(self.driver, category_button)
        video_content = self.driver.find_element(*Landing.CATEGORY_NEWS_CONTENT)
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of(video_content), 'Video category content disappear')
        first_item = self.driver.find_element(*Landing.getCategory(1))
        item_name = self.driver.execute_script(IndexScript.getCategoryName(1))
        utils.click(self.driver, first_item)
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located(SearchResult.SEARCH_RESULT), 'Cannot enter into searchResult Page')
        category_title = self.driver.execute_script(SearchResultScript.CATEGORY_TITLE)
        self.assertTrue(item_name==category_title, 'Category title not true')
  
#     def test_category_image(self):
#         category_button = self.driver.find_element(*Landing.CATEGORY_IMAGE)
#         category_button.click()
#         first_item = self.driver.find_element(*Landing.getCategory(1))
#         assert first_item.is_displayed()
#         item_name = self.driver.execute_script(IndexScript.getCategoryName(1))
#         first_item.click()
#         assert 'categoryType=image' in self.driver.current_url
#         category_title = self.driver.execute_script(SearchResultScript.CATEGORY_TITLE)
#         assert item_name == category_title

    @unittest.skip("must skipping")
    def test_category_training(self):
        category_button = self.driver.find_element(*Landing.CATEGORY_TRAINING)
        category_button.click()
        first_item = self.driver.find_element(*Landing.getCategory(1))
        assert first_item.is_displayed()
        item_name = self.driver.execute_script(IndexScript.getCategoryName(1))
        first_item.click()
        url = self.driver.current_url
        if '/category' in url:
            assert 'category.training' in url
            category_title = self.driver.execute_script(CategoryScript.CATEGORY_TITLE)
            assert category_title == item_name
        elif '/searchResults' in url:
            pass
        else:
            pass

    def test_go_top(self):
        go_top = self.driver.find_element(*Landing.GO_TOP)
        self.assertFalse(go_top.is_displayed())
        self.driver.execute_script(BaseScript.SCROLL_BUTTON)
        WebDriverWait(self.driver, 2).until(EC.visibility_of(go_top), 'Go_top button disappear')
        utils.click(self.driver, go_top)
        WebDriverWait(self.driver, 2).until_not(EC.visibility_of(go_top), 'Go_top button still display')

# class YunzhidaoCategory(unittest.TestCase):
# 
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = utils.browser()
# 
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
# 
#     def setUp(self):
#         utils.getIndex(self.driver)
# 
#     def tearDown(self):
#         pass
# 
#     def test_1(self):
#         pass

# class YunzhidaoSearchResult(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = utils.browser()
# 
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
# 
#     def setUp(self):
#         utils.getIndex(self.driver)
# 
#     def tearDown(self):
#         pass
# 
#     def test_1(self):
#         pass

if __name__ == "__main__":
    with open(config.LOG_FILE, 'a') as f:
        f.write('\n**********************************************************************\n')
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        f.write('\n**********************************************************************\n')
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner)