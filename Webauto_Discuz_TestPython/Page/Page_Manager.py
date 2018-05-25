class page_manager:
    # 创建新版块
    # 管理中心
    MANAGER_LINK_MANAGER = "xpath=>//*[@id=\"um\"]/p[1]/a[6]"
    # 登录管理账号后台
    # 用户名
    MANAGER_INPUT_LOGINNAME = "name=>admin_username"
    # 密码
    MANAGER_INPUT_LOGINPWD = "name=>admin_password"
    # 提交按钮
    MANAGER_BUTTON_LOGINSUBMIT = "name=>submit"
    # 论坛
    MANAGER_LINK_FORUM = "id=>header_forum"
    # 添加新版块
    MANAGER_LINK_ADDMOD = "linktext=>添加新版块"
    # 版块名称文本框
    MANAGER_LINK_ADDMODNAME = "xpath=>//*[@id=\"cpform\"]/table/tbody[3]/tr[1]/td[3]/div/input"
    # 论坛iframeID
    MANAGER_IFRAME_FORUM = "main"
    # 提交按钮
    MANAGER_BUTTON_SUMIT = "name=>editsubmit"