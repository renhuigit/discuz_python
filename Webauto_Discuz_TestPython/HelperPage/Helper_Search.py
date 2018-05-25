from Util.seleniumUtil import seleniumutil as seleniumUtil
from Page.Page_Search import page_search


class Helper_Search:
    # 输入搜索内容
    @classmethod
    def sendSeachContent(cls, searchContent):
        seleniumUtil.wait_element(page_search.SEARCH_TEXT_SEARCHTXT)
        seleniumUtil.sendKeys(page_search.SEARCH_TEXT_SEARCHTXT, searchContent)

    # 点击搜索按钮
    @classmethod
    def clickSearchButton(cls):
        seleniumUtil.wait_element(page_search.SEARCH_BUTTON_SEARCHBUTTON)
        seleniumUtil.click(page_search.SEARCH_BUTTON_SEARCHBUTTON)

    # 搜索类型，默认搜索帖子
    # 点击搜索的帖子
    @classmethod
    def clickSearchPosting(cls):
        seleniumUtil.wait_element(page_search.SEARCH_LINK_POSTINGS)
        seleniumUtil.click(page_search.SEARCH_LINK_POSTINGS)

    # 验证是否相同
    @classmethod
    def isExcepted(cls, exceptedContent):
        seleniumUtil.wait_element(page_search.SEARCH_LINK_POSTINGSTITLE)
        elements = seleniumUtil.getElements(page_search.SEARCH_LINK_POSTINGSTITLE)
        for element in elements:
            seleniumUtil.assertForText(element, exceptedContent)

    # 重构搜索方法并验证默认搜索帖子
    @classmethod
    def search(cls, searchContent):
        cls.sendSeachContent(searchContent)
        cls.clickSearchButton()
        seleniumUtil.switchToNewWindow()
        cls.clickSearchPosting()
        seleniumUtil.switchToNewWindow()
        cls.isExcepted(searchContent)

    # 选择搜索类型：用户 / 贴子 / 本版搜索
    @classmethod
    def selectSearchType(cls, value):
        seleniumUtil.wait_element(page_search.SEARCH_SELECT_SEARCHTYPE)
        seleniumUtil.click(page_search.SEARCH_SELECT_SEARCHTYPE)
        seleniumUtil.click(value)

    # 重构搜索方法搜索其他类型
    @classmethod
    def searchUser(cls, searchContent, value):
        cls.sendSeachContent(searchContent)
        cls.selectSearchType(value)
        cls.clickSearchButton()
