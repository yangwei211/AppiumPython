# coding=utf-8
# import Base


class loginPage():
    def __init__(self,driver):
        self.driver=driver
    #driver = Base.Base.driver

    # # 登录方式-注册
    # def register(self):
    #     return self.driver.find_element_by_id("com.guokr.mentor:id/button_register_tab")

    # # 登录方式-登录
    # def login(self):
    #     return self.driver.find_element_by_id("com.guokr.mentor:id/button_login_tab")

    # 账号输入框
    def username(self, username):
        return self.driver.find_element_by_id(username)

    # 密码输入框
    def password(self, password):
        return self.driver.find_element_by_id(password)

    # 登录按钮
    def enter(self):
        return self.driver.find_element_by_id("yui-gen1-button")

    # 清除输入框数据
    def username_Clear(self):
        username = self.username()
        username.clear()

    def login(self, username, password):
        self.username(username)
        self.password(password)
        self.enter()

