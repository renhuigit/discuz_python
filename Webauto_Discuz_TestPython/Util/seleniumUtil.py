from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Util.LogConfigeration import Logger
from selenium import webdriver

# 日志
logger = Logger(logger="seleniumutil").getlog()


class seleniumutil:
    driver = webdriver.Remote

    # 获取驱动
    @classmethod
    def getWebdriver(cls, type):
        if type == "chrome":
            cls.driver = webdriver.Chrome("D:/maven-3.0.5/chromedriver.exe")
            logger.info("开启谷歌浏览器")
            return cls.driver
        if type == "firefox":
            cls.driver = webdriver.Firefox("D:/maven-3.0.5/chromedriver.exe")
            logger.info("开启火狐浏览器")
            return cls.driver
        else:
            logger.error("未识别驱动")
            return None

    # 打开网址
    @classmethod
    def getUrl(cls, url):
        logger.info("打开网址：" + url)
        return cls.driver.get(url)

    # 查找一个元素
    @classmethod
    def getElement(cls, by):
        result = by.split('=>')
        try:
            if result[0] == "id":
                logger.info("通过id查找元素： " + by)
                return cls.driver.find_element_by_id(result[1])
            if result[0] == "class":
                logger.info("通过class查找元素： " + by)
                return cls.driver.find_element_by_class_name(result[1])
            if result[0] == "css":
                logger.info("通过css查找元素： " + by)
                return cls.driver.find_elements_by_css_selector(result[1])
            if result[0] == "linktext":
                logger.info("通过linktext查找元素： " + by)
                return cls.driver.find_element_by_link_text(result[1])
            if result[0] == "partiallinktext":
                logger.info("通过plinktext查找元素： " + by)
                return cls.driver.find_element_by_partial_link_text(result[1])
            if result[0] == "name":
                logger.info("通过name查找元素： " + by)
                return cls.driver.find_element_by_name(result[1])
            if result[0] == "xpath":
                logger.info("通过xpath查找元素： " + by)
                return cls.driver.find_element_by_xpath(result[1])
            if result[0] == "value":
                logger.info("通过value查找元素： " + by)
                return cls.driver.find_element(result[1])
            else:
                logger.info("没有找到查找类型")
        except Exception:
            logger.error("没有找到元素")
            return "抛出异常"

    # 点击元素
    @classmethod
    def click(cls, by):
        seleniumutil.getElement(by).click()
        logger.info("成功点击元素")

    # 刷新页面
    @classmethod
    def refresh(cls):
        seleniumutil.driver.refresh()

    # 清除文本框内容
    @classmethod
    def clear(cls, by):
        seleniumutil.getElement(by).clear()
        logger.info("成功清除文本框内容")

    # 输入文本
    @classmethod
    def sendKeys(cls, by, sendcontent):
        seleniumutil.clear(by)
        seleniumutil.getElement(by).send_keys(sendcontent)
        logger.info("在文本框输入" + sendcontent)

    # 获取文本
    @classmethod
    def getText(cls, by):
        logger.info("获取文本内容" + seleniumutil.getElement(by).text)
        return seleniumutil.getElement(by).text

    # 查找一组元素
    @classmethod
    def getElements(cls, by):
        result = by.split('=>')
        try:
            if result[0] == "id":
                logger.info("通过Id查找到一组元素:  " + by + "长度为：" + str(len(cls.driver.find_elements_by_id(result[1]))))
                return cls.driver.find_elements_by_id(result[1])
            if result[0] == "tagname":
                logger.info(
                    "通过tagname查找到一组元素:  " + by + "长度为：" + str(len(cls.driver.find_element_by_tag_name(result[1]))))
                return cls.driver.find_element_by_tag_name(result[1])
            if result[0] == "class":
                logger.info(
                    "通过classname查找到一组元素:  " + by + "长度为：" + str(len(cls.driver.find_elements_by_class_name(result[1]))))
                return cls.driver.find_elements_by_class_name(result[1])
            if result[0] == "css":
                logger.info("通过cssselector查找到一组元素:  " + by + "长度为：" + str(
                    len(cls.driver.find_elements_by_css_selector(result[1]))))
                return cls.driver.find_elements_by_css_selector(result[1])
            if result[0] == "linktext":
                logger.info(
                    "通过linktext查找到一组元素:  " + by + "长度为：" + str(len(cls.driver.find_elements_by_link_text(result[1]))))
                return cls.driver.find_elements_by_link_text(result[1])
            if result[0] == "plinktext":
                logger.info("通过partiallinktext查找到一组元素:  " + by + "长度为：" + str(
                    len(cls.driver.find_elements_by_partial_link_text(result[1]))))
                return cls.driver.find_elements_by_partial_link_text(result[1])
            if result[0] == "name":
                logger.info("通过name查找到一组元素:  " + by + "长度为：" + str(len(cls.driver.find_elements_by_name(result[1]))))
                return cls.driver.find_elements_by_name(result[1])
            if result[0] == "xpath":
                logger.info("通过xpath查找到一组元素:  " + by + "长度为：" + str(len(cls.driver.find_elements_by_xpath(result[1]))))
                return cls.driver.find_elements_by_xpath(result[1])
            if result[0] == "value":
                logger.info("通过value查找到一组元素:  " + by + "长度为：" + str(len(cls.driver.find_elements(result[1]))))
                return cls.driver.find_elements(result[1])
            else:
                logger.info("没有找到查找类型")
        except Exception:
            logger.error("查找到一组元素失败")
            return None

    @classmethod
    def assertPage(cls, exceptedContent):
        actual = seleniumutil.driver.title
        if actual == exceptedContent:
            logger.info("找到了对应得title，当前页面正确：【" + actual + "】")
        else:
            logger.error("未找到了对应的title，当前页面是：【" + actual + "】，期望页面是：【" + exceptedContent + "】")

    # 切换框架
    @classmethod
    def switchToFrame(cls, frameId):
        # 封装进入id = value的frame中
        cls.driver.switch_to.frame(frameId)
        logger.info("成功切换iframe，切换的frameID为" + frameId)

    # 切换默认iframe主文档
    @classmethod
    def switchToDefaultContent(cls):
        # 封装跳出iframe，进入defaultcontent
        cls.driver.switch_to.default_content()
        logger.info("跳出iframe，进入主文档")

    # 切换新窗口
    @classmethod
    def switchToNewWindow(cls):
        handles = cls.driver.window_handles
        i = len(handles)
        cls.driver.switch_to.window(handles[i - 1])
        logger.info("成功切换窗口，当前窗口标题为" + cls.driver.title)

    # 判断文本是否相同
    @classmethod
    def assertForText(cls, element, exceptedContent):
        actual = element.text
        if actual == exceptedContent:
            logger.info("找到了对应得文本，当前页面正确：【" + actual + "】")
        else:
            logger.error("当前页面是：【" + actual + "】，期望页面是：【" + exceptedContent + "】")

    @classmethod
    def wait_element(cls, str, seconds=10):
        if "=>" not in str:
            raise NameError("定义错误以'=>'.为分隔符")
        by = str.split("=>")[0]
        value = str.split("=>")[1]
        if by == "id":
            WebDriverWait(cls.driver, seconds, 1).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(cls.driver, seconds, 1).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(cls.driver, seconds, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "linktext":
            WebDriverWait(cls.driver, seconds, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(cls.driver, seconds, 1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(cls.driver, seconds, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        elif by == "plinktext":
            WebDriverWait(cls.driver, seconds, 1).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)))
        else:
            raise NameError("请正确填写查找类型")
