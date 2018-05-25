class page_vote:
    # 单选框按钮
    VOTE_RADIO_VOTE = "xpath=>//td[@class=\"pslt\"]/input"

    # 提交按钮
    VOTE_BUTTON_SUBMIT = "id=>pollsubmit"

    # 票数信息、投票比例
    VOTE_LINK_MESSAGE = "xpath=>//table[@summary=\"poll panel\"]/tbody/tr/td[2]"

    # 选项名称
    VOTE_LINK_OPTIONNAME = "xpath=>//table/tbody/tr/td[@class=\"pvt\"]"

    # 投票主题名称
    VOTE_LINK_TITLE = "id=>thread_subject"

    # 判断是否投票
    is_vote = "xpath=>//*[@id=\"poll\"]/div[2]/table/tbody/tr[7]/td"