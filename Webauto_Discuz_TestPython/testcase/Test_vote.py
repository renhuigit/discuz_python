from testcase.BasicTestCase import BasicTestCase
from HelperPage.Helper_Vote import Helper_Vote
from HelperPage.Helper_Pulish import Helper_Publish
from HelperPage.Helper_Login import Helper_login
from HelperPage.Helper_Reply import Helper_Reply
import time


class test_Vote(BasicTestCase):
    # 发表投票帖子
    # 进行投票
    # 取出投票各个选项的名称以及投票比例
    # 取出投票的主题名称
    def test_vote(self):
        Helper_login.login("test", "test")
        list = ["这就是街舞", "热血街舞团", "创造101"]
        Helper_Publish.clickPublishInOther(1)
        i = Helper_Publish.returntopicCount()
        # 发表投票帖子
        Helper_Publish.voteByButton("投票内容：这就是街舞，热血街舞团，创造101", "网综节目投票", list)
        Helper_Publish.clickblock()
        j = Helper_Publish.returntopicCount()
        if i < j:
            print("发表投票帖子成功")
        else:
            print("发表投票帖子失败")
        # 进行投票
        Helper_Reply.clickFirstPosting()
        Helper_Vote.vote(0)
        Helper_Vote.isvote()
        # 取出投票的主题名称
        voteTitle = Helper_Vote.getVoteTitle()
        # 取出投票各个选项的名称以及投票比例
        list1 = Helper_Vote.getNumberOfVotes()
        name = Helper_Vote.getOptionName()
        print(voteTitle)
        for listcontent in list1:
            print(listcontent)
        for namecontent in name:
            print(namecontent)
