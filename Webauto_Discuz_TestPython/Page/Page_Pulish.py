class page_pulish:
    # 快速发帖
    # 快速发帖标题文本框
    publish_textarea_title = "id=>subject"

    # 快速发帖发表内容文本框
    publish_textarea_content = "id=>fastpostmessage"

    # 快速发帖发表贴子按钮
    publish_btn_publishsubmit = "id=>fastpostsubmit"

    # 发帖按钮
    pulish_btn = "id=>newspecial"

    # 发起投票连接
    PUBLISH_LINK_VOTE = "linktext=>发起投票"

    # 帖子标题
    PUBLISH_TEXT_VOTETITLE = "id=>subject"

    # 帖子内容
    PUBLISH_TEXT_VOTECONTENT = "xpath=>/html/body"

    # 发表按钮
    PUBLISH_BUTTON_SUBMITBYBUTTON = "id=>postsubmit"

    # 投票选项
    VOTE_INPUT_OPTION = "xpath=>//p/input[@name=\"polloption[]\"]"

    # 主题数量
    TOPIC_TEXT_NUM = "xpath=>//*[@id=\"ct\"]/div/div[1]/div/h1/span/strong[2]"

    # 回复数量
    REPLYADMIN_TEXT_NUM = "xpath=>//tr/td[4]/a"

    REPLY_TEXT_NUM = "xpath=>//tr/td[3]/a"


    # 发表主题后点击版块
    block_name = "xpath=>//*[@id=\"pt\"]/div/a[4]"
    # block_name = "css=>#pt div a:nth-child(7)"


