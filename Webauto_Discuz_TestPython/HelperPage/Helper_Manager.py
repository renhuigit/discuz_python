from Util.seleniumUtil import seleniumutil as seleniumUtil
from Page.Page_Manager import page_manager
import time


class Helper_Manager:

    # 点击管理中心
    @classmethod
    def clickManagerCenter(cls):
        seleniumUtil.click(page_manager.MANAGER_LINK_MANAGER)

    # 输入密码
    @classmethod
    def sendLoginPwd(cls, password):
        seleniumUtil.switchToNewWindow()
        seleniumUtil.sendKeys(page_manager.MANAGER_INPUT_LOGINPWD, password)

    # 点击登录提交按钮
    @classmethod
    def clickSubmit(cls):
        seleniumUtil.click(page_manager.MANAGER_BUTTON_LOGINSUBMIT)

    # 前台已登录点击管理中心登录后台
    @classmethod
    def loginPwdSubmit(cls, password):
        cls.clickManagerCenter()
        time.sleep(2)
        cls.sendLoginPwd(password)
        cls.clickSubmit()


    # 添加新版块
    # 点击论坛
    @classmethod
    def clickForum(cls):
        time.sleep(2)
        seleniumUtil.click(page_manager.MANAGER_LINK_FORUM)
        time.sleep(2)

    # 点击添加新版块
    @classmethod
    def clickaddBlock(cls):
        seleniumUtil.switchToFrame(page_manager.MANAGER_IFRAME_FORUM)
        seleniumUtil.wait_element(page_manager.MANAGER_LINK_ADDMOD)
        seleniumUtil.click(page_manager.MANAGER_LINK_ADDMOD)

    # 输入版块名称
    @classmethod
    def sendBlockName(cls, name):
        seleniumUtil.wait_element(page_manager.MANAGER_LINK_ADDMODNAME)
        seleniumUtil.sendKeys(page_manager.MANAGER_LINK_ADDMODNAME, name)

    # 提交修改
    @classmethod
    def submitAddBlock(cls):
        seleniumUtil.wait_element(page_manager.MANAGER_BUTTON_SUMIT)
        seleniumUtil.click(page_manager.MANAGER_BUTTON_SUMIT)

    # 重构添加新版块方法
    @classmethod
    def addBlock(cls, name):
        cls.clickForum()
        cls.clickaddBlock()
        cls.sendBlockName(name)
        cls.submitAddBlock()
