from testcase.BasicTestCase import BasicTestCase
from HelperPage.Helper_Login import Helper_login
from HelperPage.Helper_Logout import Helper_Logout
from HelperPage.Helper_Search import Helper_Search
import time


class test_Search(BasicTestCase):
    # 用户登录
    # 进行帖子搜索
    # 搜索selenium+java帖子
    # 进入搜索的帖子
    # 验证帖子标题和期望的一致
    # 用户退出
    def test_search(self):
        Helper_login.login("admin", "password")
        Helper_Search.search("selenium+java")
        Helper_Logout.clickLogout()