# 导包
from page.page_login import PageLogin
from tool.get_driver import GetDriver


class PageIn:
    """统一工厂类"""

    def __init__(self):
        self.driver = GetDriver.get_driver()

    def get_page_login(self):
        """实例化页面对象"""
        return PageLogin()


