from Util.seleniumUtil import seleniumutil as seleniumUtil
from Page.Page_Reply import page_reply
import time


class Helper_Reply:
    # 快速回复
    # 点击默认板块
    @classmethod
    def clickDefultBloc(cls):
        seleniumUtil.wait_element(page_reply.COMMENT_LINK_BLOCK)
        seleniumUtil.click(page_reply.COMMENT_LINK_BLOCK)

    # 点击第一条帖子
    @classmethod
    def clickFirstPosting(cls):
        seleniumUtil.wait_element(page_reply.COMMENT_LINK_POSTINGS)
        seleniumUtil.click(page_reply.COMMENT_LINK_POSTINGS)

    # 输入回复内容
    @classmethod
    def sendReply(cls, reply):
        seleniumUtil.wait_element(page_reply.COMMENT_TEXTAREA_MESSAGE)
        seleniumUtil.sendKeys(page_reply.COMMENT_TEXTAREA_MESSAGE, reply)

    # 点击回复按钮
    @classmethod
    def clickReplySubmit(cls):
        seleniumUtil.wait_element(page_reply.COMMENT_BUTTON_REPLYSUBMIT)
        seleniumUtil.click(page_reply.COMMENT_BUTTON_REPLYSUBMIT)

    # 快速回复方法重构
    @classmethod
    def replyQuickly(cls, content):
        # cls.clickDefultBloc()
        cls.clickFirstPosting()
        cls.sendReply(content)
        seleniumUtil.wait_element(page_reply.reply_check_fresh)
        seleniumUtil.click(page_reply.reply_check_fresh)
        cls.clickReplySubmit()
        time.sleep(2)
        seleniumUtil.refresh()
