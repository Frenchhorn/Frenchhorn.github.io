class BaseScript():
    ISWEIXIN = 'return yunzhidao.config.isWeixin'
    SCROLL_TOP = '$(document).scrollTop(0)'
    SCROLL_BUTTON = '$(document).scrollTop(10000)'

class IndexScript():
    """Scripts for Index page"""
    SEARCHTYPE = """return $('input[name="searchType"]:checked').val()"""

    @staticmethod
    def getCategoryName(n):
        return "return $('.am-tabs .am-active li:nth-child({})').text().trim()".format(n)

class SearchInputScript():
    """Scripts for SearchInput page"""
    SEARCHTYPE = """return $('input[name="searchType"]:checked').val()"""

class SearchResultScript():
    CATEGORY_TITLE = 'return $("header .title").text().trim()'

class CategoryScript():
    CATEGORY_TITLE = 'return $("header span").text().trim()'