from selenium.webdriver.common.by import By
'''
 |  CLASS_NAME = 'class name'
 |
 |  CSS_SELECTOR = 'css selector'
 |
 |  ID = 'id'
 |
 |  LINK_TEXT = 'link text'
 |
 |  NAME = 'name'
 |
 |  PARTIAL_LINK_TEXT = 'partial link text'
 |
 |  TAG_NAME = 'tag name'
 |
 |  XPATH = 'xpath'
'''

class BasePage():
    GO_TOP = (By.CSS_SELECTOR, '.am-gotop-icon')

class Landing(BasePage):
    """A class for index page locators. All index page locators should come here"""
    LANDING = (By.ID, 'landingPage')

    SEARCHTYPE_ALL = (By.CSS_SELECTOR, '.option-group label:nth-child(1)')
    SEARCHTYPE_ALL_INPUT = (By.CSS_SELECTOR, '#option1')
    SEARCHTYPE_VIDEO = (By.CSS_SELECTOR, '.option-group label:nth-child(2)')
    SEARCHTYPE_VIDEO_INPUT = (By.CSS_SELECTOR, '#option2')
    SEARCHTYPE_IMAGE = (By.CSS_SELECTOR, '.option-group label:nth-child(3)')
    SEARCHTYPE_IMAGE_INPUT = (By.CSS_SELECTOR, '#option3')

    SEARCH_BAR = (By.CSS_SELECTOR, '.am-input-group')

    CATEGORY_NEWS = (By.CSS_SELECTOR, '[categorytype=news]')
    CATEGORY_NEWS_CONTENT = (By.CSS_SELECTOR, '#news')
    CATEGORY_VIDEO = (By.CSS_SELECTOR, '[categorytype=video]')
    CATEGORY_VIDEO_CONTENT = (By.CSS_SELECTOR, '#video')
    CATEGORY_IMAGE = (By.CSS_SELECTOR, '[categorytype=image]')
    CATEGORY_IMAGE_CONTENT = (By.CSS_SELECTOR, '#image')
    CATEGORY_TRAINING = (By.CSS_SELECTOR, '[categorytype=training]')
    CATEGORY_TRAINING_CONTENT = (By.CSS_SELECTOR, '#training')

    @staticmethod
    def getCategory(n):
        return (By.CSS_SELECTOR ,'.am-tabs .am-active li:nth-child({})'.format(n))

    @staticmethod
    def getInfoList(a, b=0):
        if b==0:
            return (By.CSS_SELECTOR, '.info-list li:nth-child({})'.format(a))
        elif b==1:
            return (By.CSS_SELECTOR, '.info-list li:nth-child({}) .abs-con a'.format(a))
        elif b==2:
            return (By.CSS_SELECTOR, '.info-list li:nth-child({}) .btn-generalize'.format(a))
    CHANGE = (By.ID, 'changeDailyUpdate')

    @staticmethod
    def getHotword(a):
        return (By.CSS_SELECTOR, '.hot-keys_index a:nth-child({})'.format(a))

class SearchInput(BasePage):
    """A class for searchInput page locators. All searchResult locators should come here"""
    SEARCH_INPUT = (By.CSS_SELECTOR, '#searchInputPage')

    SEARCHTYPE_ALL = (By.CSS_SELECTOR, '.option-group label:nth-child(1)')
    SEARCHTYPE_VIDEO = (By.CSS_SELECTOR, '.option-group label:nth-child(2)')
    SEARCHTYPE_IMAGE = (By.CSS_SELECTOR, '.option-group label:nth-child(3)')
    BACK_BUTTON = (By.CSS_SELECTOR, '#btn-home')

class SearchResult(BasePage):
    """A class for searchResult page locators. All searchResult locators should come here"""
    SEARCH_RESULT = (By.CSS_SELECTOR, '#searchResultPage')

    SEARCHTYPE_ALL = (By.CSS_SELECTOR, '.option-group label:nth-child(1)')
    SEARCHTYPE_VIDEO = (By.CSS_SELECTOR, '.option-group label:nth-child(2)')
    SEARCHTYPE_IMAGE = (By.CSS_SELECTOR, '.option-group label:nth-child(3)')
    HOME_BUTTON = (By.CSS_SELECTOR, '。icon_home')

    SEARCH_TEXT = (By.CSS_SELECTOR, '#autocomplete')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '[onclick=onSearchClick();]')

    CH_BUTTON = (By.CSS_SELECTOR, '[onclick=onPromotionFilterClick();]')
    FLOW_BUTTON = (By.CSS_SELECTOR, '[onclick=onTimeSortFilterClick();]')
    TIME_BUTTON = (By.CSS_SELECTOR, '[onclick=onFlowSortFilterClick();]')

    @staticmethod
    def getSearchResult(a, b=0):
        if b==0:
            return (By.CSS_SELECTOR, '.results-wrapper ')

    @staticmethod
    def getImageSearch(a=0):
        pass

    @staticmethod
    def getRelatedKeyword(a):
        return (By.CSS_SELECTOR, '.related-keywords a:nth-child({})'.format(a))

    FIRST_PAGE = (By.CSS_SELECTOR, '#first-page')
    PREV_PAGE = (By.CSS_SELECTOR, '#prev-page')
    NEXT_PAGE = (By.CSS_SELECTOR, '#next-page')
    LAST_PAGE = (By.CSS_SELECTOR, '#last-page')

class Category(BasePage):
    """A class for category page locators. All category locators should come here"""
    CATEGORY = (By.CSS_SELECTOR, '#categoryPage')

    @staticmethod
    def getCategory(a):
        return (By.CSS_SELECTOR, 'sub-lable-list li:nth-child({})'.format(a))