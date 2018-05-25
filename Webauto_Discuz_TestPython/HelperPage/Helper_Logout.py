from Util.seleniumUtil import seleniumutil
from Page.Page_home import page_home


class Helper_Logout:
    # 前端点击退出
    @classmethod
    def clickLogout(cls):
        seleniumutil.wait_element(page_home.logout)
        seleniumutil.click(page_home.logout)

    # 后台登出
    @classmethod
    def clickAdminLogout(cls):
        seleniumutil.switchToDefaultContent()
        seleniumutil.wait_element(page_home.logout)
        seleniumutil.click(page_home.logout)
