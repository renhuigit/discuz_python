
class page_reply:
    # 默认板块
    COMMENT_LINK_BLOCK = "xpath=>//*[@id='category_1']/table/tbody/tr[1]/td[2]/h2/a"
    # 帖子
    COMMENT_LINK_POSTINGS = "xpath=>//*[@class='s xst']"
    # 回复
    COMMENT_LINK_REPLY = "linkText=>回复"
    # 回帖文本框
    COMMENT_TEXTAREA_MESSAGE = "name=>message"
    # 发表回复按钮
    COMMENT_BUTTON_REPLYSUBMIT = "xpath=>//button[@name='replysubmit']"
    # 回复选择选择框跳到最后一页
    reply_check_fresh = "id=>fastpostrefresh"