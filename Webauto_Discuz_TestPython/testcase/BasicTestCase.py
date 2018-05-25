import os
from unittest import TestCase
from selenium import webdriver
from Util.LogConfigeration import Logger
from Util.seleniumUtil import seleniumutil
from configparser import ConfigParser

logger = Logger(logger="BasicTestCase").getlog()


class BasicTestCase(TestCase):
    driver = webdriver.Remote
    # 读取config文件
    config = ConfigParser()
    # file_path = os.path.dirname(os.getcwd()) + '/config/config'
    file_path = os.path.dirname(os.path.abspath('.')) + '/config/config'
    config.read(file_path)
    browser = config.get("browserType", "browserName")
    logger.info("你选择了 %s 浏览器." % browser)
    url = config.get("testServer", "URL")
    logger.info("测试的URL是: %s" % url)

    def setUp(self):
        BasicTestCase.driver = seleniumutil.getWebdriver(BasicTestCase.browser)
        seleniumutil.getUrl(BasicTestCase.url)

    def tearDown(self):
        BasicTestCase.driver.quit()
        pass
        logger.info("退出浏览器")
