from Util.seleniumUtil import seleniumutil as seleniumUtil
from Page.Page_Vote import page_vote


class Helper_Vote:
    # 选择选项
    @classmethod
    def clickChoiceMessage(cls, i):
        seleniumUtil.wait_element(page_vote.VOTE_RADIO_VOTE)
        element = seleniumUtil.getElements(page_vote.VOTE_RADIO_VOTE)
        element[i].click()

    # 点击投票
    @classmethod
    def clickPollSubmit(cls):
        seleniumUtil.wait_element(page_vote.VOTE_BUTTON_SUBMIT)
        seleniumUtil.click(page_vote.VOTE_BUTTON_SUBMIT)

    # 重构投票方法
    @classmethod
    def vote(cls, i):
        cls.clickChoiceMessage(i)
        cls.clickPollSubmit()

    # 获取票数比例
    @classmethod
    def getNumberOfVotes(cls):
        seleniumUtil.wait_element(page_vote.VOTE_LINK_MESSAGE)
        elements = seleniumUtil.getElements(page_vote.VOTE_LINK_MESSAGE)
        i = 0
        votes = []
        for element in elements:
            if (i + 1) % 2 == 0:
                votes.append(element.text)
            i += 1
        return votes

    # 获取投票主题
    @classmethod
    def getVoteTitle(cls):
        seleniumUtil.wait_element(page_vote.VOTE_LINK_TITLE)
        title = seleniumUtil.getText(page_vote.VOTE_LINK_TITLE)
        return title

    # 获取选项名称 * /
    @classmethod
    def getOptionName(cls):
        seleniumUtil.wait_element(page_vote.VOTE_LINK_OPTIONNAME)
        elements = seleniumUtil.getElements(page_vote.VOTE_LINK_OPTIONNAME)
        names = []
        for element in elements:
            names.append(element.text)
        return names

    # 判断投票是否成功
    @classmethod
    def isvote(cls):
        seleniumUtil.refresh()
        seleniumUtil.wait_element(page_vote.is_vote)
        text = seleniumUtil.getElement(page_vote.is_vote).text
        if text == "您已经投过票，谢谢您的参与":
            print("投票成功")
        else:
            print("投票失败")
