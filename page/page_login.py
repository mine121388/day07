# 导包
from base.base_login import BaseLogin
import page


class PageLogin(BaseLogin):
    """页面对象类"""

    def input_name(self, username):
        """输入用户名"""
        self.input_func(page.login_username, username)

    def input_pwd(self, pwd):
        """输入密码"""
        self.input_func(page.login_pwd, pwd)

    def click_btn(self):
        """点击登录"""
        self.click_func(page.login_btn)

    def page_login(self, username, pwd):
        """组合业务"""
        self.input_name(username)
        self.input_pwd(pwd)
        self.click_btn()
