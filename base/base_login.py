# 导包
from selenium.webdriver.support.wait import WebDriverWait

from tool.get_driver import GetDriver


class BaseLogin:
    """页面对象操作类"""

    def __init__(self):
        """初始化driver对象"""
        self.driver = GetDriver.get_driver()

    def find_element(self, loc, timeout=10, poll=1):
        """定位元素方法加显示等待"""
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def input_func(self, loc, values):
        """输入方法"""
        el = self.find_element(loc)
        el.clear()
        el.send_keys(values)

    def click_func(self, loc):
        """点击登录方法"""
        self.find_element(loc).click()
