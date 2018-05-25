from Util.seleniumUtil import seleniumutil as seleniumUtil
from Page.Page_Delete import page_delete


class HelperDelete:
    # 选择删除
    # 点击选中复选框
    @classmethod
    def clickChecked(cls, i):
        seleniumUtil.wait_element(page_delete.DELETE_CHECKED_SELECT)
        list = seleniumUtil.getElements(page_delete.DELETE_CHECKED_SELECT)
        list[i].click()

    # 点击删除
    @classmethod
    def clickDelete(cls):
        seleniumUtil.wait_element(page_delete.DELETE_LINK_DELETE)
        seleniumUtil.click(page_delete.DELETE_LINK_DELETE)

    # 点击确定删除
    @classmethod
    def clickSubmit(cls):
        seleniumUtil.wait_element(page_delete.DELETE_BUTTON_SUBMIT)
        seleniumUtil.click(page_delete.DELETE_BUTTON_SUBMIT)

    # 重构删除方法
    @classmethod
    def delete(cls, i):
        cls.clickChecked(i)
        cls.clickDelete()
        cls.clickSubmit()
