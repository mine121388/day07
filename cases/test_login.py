# 导包
import pytest
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.read_yaml import read_yaml


def data_build():
    """参数化方法"""
    return read_yaml("login.yaml")


class TestLogin:
    """自定义测试类"""

    def setup_class(self):
        """初始化页面对象"""
        self.login = PageIn().get_page_login()

    def teardown_class(self):
        """关闭driver对象"""
        GetDriver.quit_driver()

    @pytest.mark.parametrize("username,pwd", data_build())
    def test_login(self, username, pwd):
        """登录测试方法"""
        self.login.page_login(username, pwd)
