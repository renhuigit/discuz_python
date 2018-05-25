from Util.seleniumUtil import seleniumutil
from Page.Page_home import page_home
import time


class Helper_login:

    # 输入用户名
    @classmethod
    def sendUsername(cls, userName):
        seleniumutil.wait_element(page_home.username)
        seleniumutil.sendKeys(page_home.username, userName)

    # 输入密码
    @classmethod
    def sendpassword(cls, password):
        seleniumutil.wait_element(page_home.password)
        seleniumutil.sendKeys(page_home.password, password)

    # 点击登录按钮
    @classmethod
    def clickLogin(cls):
        seleniumutil.wait_element(page_home.login_btn)
        seleniumutil.click(page_home.login_btn)

    # 重构登录方法
    @classmethod
    def login(cls, userName, password):
        Helper_login.sendUsername(userName)
        Helper_login.sendpassword(password)
        Helper_login.clickLogin()
        print(Helper_login.islogin())

    # 判断是否登录
    @classmethod
    def islogin(cls):
        seleniumutil.wait_element(page_home.loginstatus)
        text = seleniumutil.getElement(page_home.loginstatus).text
        if text[0:2] == "积分":
            return "登陆成功"
        else:
            return "登录失败"
