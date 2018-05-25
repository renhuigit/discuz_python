from Util.seleniumUtil import seleniumutil
from Page.Page_Pulish import page_pulish
from Page.Page_home import page_home
import time


class Helper_Publish:

    # 根据索引点击想点击的版块
    @classmethod
    def clickPublishInOther(cls, i):
        seleniumutil.wait_element(page_home.PUBLISH_LINK_BLOCKS)
        list = seleniumutil.getElements(page_home.PUBLISH_LINK_BLOCKS)
        list[i].click()

    # 默认板块快速发帖
    # 点击默认板块
    @classmethod
    def clickDefultBlock(cls):
        seleniumutil.wait_element(page_home.defualtmode)
        seleniumutil.click(page_home.defualtmode)
        return "默认版块"

    # 输入标题
    @classmethod
    def sendTitle(cls, title):
        seleniumutil.wait_element(page_pulish.publish_textarea_title)
        seleniumutil.sendKeys(page_pulish.publish_textarea_title, title)

    # 输入帖子内容
    @classmethod
    def sendContent(cls, content):
        seleniumutil.wait_element(page_pulish.publish_textarea_content)
        seleniumutil.sendKeys(page_pulish.publish_textarea_content, content)

    # 点击发表帖子按钮
    @classmethod
    def clickPublishSubmit(cls):
        seleniumutil.wait_element(page_pulish.publish_btn_publishsubmit)
        seleniumutil.click(page_pulish.publish_btn_publishsubmit)

    # 重构快速发帖方法
    @classmethod
    def publishQuickly(cls, title, content):
        Helper_Publish.sendTitle(title)
        Helper_Publish.sendContent(content)
        Helper_Publish.clickPublishSubmit()

    # 其他板块快速发帖重构
    @classmethod
    def publishInOther(cls, title, content):
        # Helper_Publish.clickPublishInOther(i)
        Helper_Publish.sendTitle(title)
        Helper_Publish.sendContent(content)
        Helper_Publish.clickPublishSubmit()

    # 发帖按钮发帖
    # 点击发帖按钮
    @classmethod
    def clickPublishBlock(cls):
        seleniumutil.wait_element(page_pulish.pulish_btn)
        seleniumutil.click(page_pulish.pulish_btn)

    # 发帖标题文本框
    @classmethod
    def sendPublishTitle(cls, title):
        seleniumutil.wait_element(page_pulish.PUBLISH_TEXT_VOTETITLE)
        seleniumutil.sendKeys(page_pulish.PUBLISH_TEXT_VOTETITLE, title)

    # 发帖内容文本框
    @classmethod
    def sendPublishContent(cls, content):
        seleniumutil.switchToFrame("e_iframe")
        seleniumutil.wait_element(page_pulish.PUBLISH_TEXT_VOTECONTENT)
        seleniumutil.sendKeys(page_pulish.PUBLISH_TEXT_VOTECONTENT, content)

    # 点击发表帖子
    @classmethod
    def clickSubmitByButton(cls):
        seleniumutil.switchToDefaultContent()
        seleniumutil.wait_element(page_pulish.PUBLISH_BUTTON_SUBMITBYBUTTON)
        seleniumutil.click(page_pulish.PUBLISH_BUTTON_SUBMITBYBUTTON)

    # 重构发帖按钮发帖方法
    @classmethod
    def publishByButton(cls, i, content, title):
        Helper_Publish.clickPublishInOther(i)
        Helper_Publish.clickPublishBlock()
        Helper_Publish.sendPublishTitle(title)
        Helper_Publish.sendPublishContent(content)
        Helper_Publish.clickSubmitByButton()

    # 发起投票
    # 点击发起投票
    @classmethod
    def clickVote(cls):
        seleniumutil.wait_element(page_pulish.PUBLISH_LINK_VOTE)
        seleniumutil.click(page_pulish.PUBLISH_LINK_VOTE)

    # 点击添加选项链接
    @classmethod
    def addOption(cls):
        seleniumutil.wait_element(page_pulish.VOTE_LINK_ADD)
        seleniumutil.click(page_pulish.VOTE_LINK_ADD)

    # 输入选项内容
    @classmethod
    def sendOption(cls, optionContent):
        seleniumutil.wait_element(page_pulish.VOTE_INPUT_OPTION)
        list = seleniumutil.getElements(page_pulish.VOTE_INPUT_OPTION)
        i = 0
        for con in optionContent:
            list[i].send_keys(con)
            i += 1

    # 重构发起投票方法
    @classmethod
    def voteByButton(cls, content, title, optionContent):
        # Helper_Publish.clickPublishInOther(i)
        Helper_Publish.clickPublishBlock()
        Helper_Publish.clickVote()
        Helper_Publish.sendPublishTitle(title)
        Helper_Publish.sendOption(optionContent)
        Helper_Publish.sendPublishContent(content)
        Helper_Publish.clickSubmitByButton()
        time.sleep(2)

    # 返回版块数量
    @classmethod
    def returnblockscount(cls):
        seleniumutil.wait_element(page_home.PUBLISH_LINK_BLOCKS)
        list = seleniumutil.getElements(page_home.PUBLISH_LINK_BLOCKS)
        count = len(list)
        return count

    # 返回主题的数量
    @classmethod
    def returntopicCount(cls):
        seleniumutil.wait_element(page_pulish.TOPIC_TEXT_NUM)
        return int(seleniumutil.getElement(page_pulish.TOPIC_TEXT_NUM).text)

    # 返回第一个帖子回复数量
    @classmethod
    def returnreplyCount(cls):
        seleniumutil.wait_element(page_pulish.REPLY_TEXT_NUM)
        return int(seleniumutil.getElements(page_pulish.REPLY_TEXT_NUM)[1].text)

    # 返回第一个帖子回复数量
    @classmethod
    def returnadminreplyCount(cls):
        seleniumutil.wait_element(page_pulish.REPLYADMIN_TEXT_NUM)
        return int(seleniumutil.getElements(page_pulish.REPLYADMIN_TEXT_NUM)[0].text)

    # 发表后点击版块名
    @classmethod
    def clickblock(cls):
        seleniumutil.wait_element(page_pulish.block_name)
        seleniumutil.click(page_pulish.block_name)