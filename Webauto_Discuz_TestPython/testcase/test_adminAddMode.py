from testcase.BasicTestCase import BasicTestCase
from HelperPage.Helper_Login import Helper_login
from HelperPage.Helper_Logout import Helper_Logout
from HelperPage.Helper_Pulish import Helper_Publish
from HelperPage.Helper_Reply import Helper_Reply
from HelperPage.Helper_Delete import HelperDelete
from Util.seleniumUtil import seleniumutil
from HelperPage.Helper_Manager import Helper_Manager
import time


class test_adminAddMode(BasicTestCase):
    # 管理员用户登录
    # 进入默认板块，删除帖子
    # 进入版块管理(管理中心 - -论坛)
    # 创建新的版块
    # 管理员退出
    # 普通用户登录
    # 在版块下发帖
    # 回复帖子

    def testadmin(self):
        # 管理员用户登录
        Helper_login.login("admin", "password")
        i = Helper_Publish.returnblockscount()
        Helper_Publish.clickPublishInOther(1)
        m = Helper_Publish.returntopicCount()
        # 进入默认板块，删除帖子
        HelperDelete.delete(2)
        n = Helper_Publish.returntopicCount()
        if m > n:
            print("删除主题成功")
        else:
            print("删除主题失败")
        # 进入版块管理(管理中心 - -论坛)
        # 创建新的版块
        Helper_Manager.loginPwdSubmit("password")
        Helper_Manager.addBlock("诗意盎然")
        # 管理员退出
        Helper_Logout.clickAdminLogout()
        seleniumutil.switchToNewWindow()
        j = Helper_Publish.returnblockscount()
        if i < j:
            print("添加新版块成功")
        else:
            print("添加新版块失败")
        Helper_Logout.clickLogout()
        # 普通用户登录
        Helper_login.login("test", "test")
        Helper_Publish.clickPublishInOther(2)
        i = Helper_Publish.returntopicCount()
        # 在版块下发帖
        Helper_Publish.publishInOther("selenium+java", "testng+selenium框架")
        Helper_Publish.clickblock()
        m = Helper_Publish.returnreplyCount()
        time.sleep(10)
        # 回复帖子
        Helper_Reply.replyQuickly("selenium+testng+java框架")
        Helper_Publish.clickblock()
        j = Helper_Publish.returntopicCount()
        if i < j:
            print("发表成功，帖子的数量是" + str(j))
        else:
            print("发表失败")
        n = Helper_Publish.returnreplyCount()
        if m < n:
            print("回复成功，回复的数量是" + str(n))
        else:
            print("回复失败")
        Helper_Logout.clickLogout()
        time.sleep(2)
