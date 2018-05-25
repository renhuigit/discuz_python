from testcase.BasicTestCase import BasicTestCase
from HelperPage.Helper_Login import Helper_login
from HelperPage.Helper_Logout import Helper_Logout
from HelperPage.Helper_Pulish import Helper_Publish
from HelperPage.Helper_Reply import Helper_Reply
import time


class testLogin(BasicTestCase):
    # 用户登录
    # 默认板块发帖
    # 默认板块回帖
    # 用户退出
    def test_login(self):
        # 用户登录
        Helper_login.login("admin", "password")
        Helper_Publish.clickDefultBlock()
        i = Helper_Publish.returntopicCount()
        # 默认板块发帖
        Helper_Publish.publishQuickly("title:title", "content:content")
        Helper_Publish.clickblock()
        m = Helper_Publish.returnadminreplyCount()
        # 默认板块回帖
        Helper_Reply.replyQuickly("回复内容")
        Helper_Publish.clickblock()
        j = Helper_Publish.returntopicCount()
        if i < j:
            print("发表成功，帖子的数量是" + str(j))
        else:
            print("发表失败")
        n = Helper_Publish.returnadminreplyCount()
        if m < n:
            print("回复成功，回复的数量是" + str(n))
        else:
            print("回复失败")
        # 用户退出
        Helper_Logout.clickLogout()
        time.sleep(2)
