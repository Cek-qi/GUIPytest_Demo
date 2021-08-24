# coding=utf-8
# 登录页面
# url:tz-e1-management-front/#/
import traceback
from DesignSpace.TestFunction.public.public_debug import *
from DesignSpace.TestFunction.public.public_WaitElement import FindElement
from DesignSpace.TestFunction.public.public_urlcheck import urlcheck
from selenium import webdriver


class loginPage(FindElement):
    Username = '//*[@id="app"]/div/div[2]/div[2]/form/div[1]/div/div[1]/input'
    Password = '//*[@id="app"]/div/div[2]/div[2]/form/div[2]/div/div[1]/input'
    LoginButton = '//*[@id="keybtn"]/span'
    continued = '/html/body/div[1]/div/div[2]/div/div[1]/span[2]/a'


    def __init__(self,session):
        FindElement.__init__(self, session)
        self.session = session

    def input_userName(self, name):
        '''输入用户名'''
        self.public_WaitElementXpath(self.Username)[0].send_keys(name)

    def input_passWord(self, passWord):
        '''输入密码'''
        self.public_WaitElementXpath(self.Password)[0].send_keys(passWord)

    def click_loginButton(self):
        '''点击登陆按钮'''
        self.public_WaitElementXpath(self.LoginButton)[0].click()

    def urlJump(self, url):
        '''url跳转'''
        self.session.get(url)

    def click_continue(self):
        '''忽略'''
        self.public_WaitElementXpath(self.continued)[0].click()

    def urlEffect(self):
        try:
            urlcheck(self.session, "ezview")
            return 1
        except:
            print(traceback.print_exc())
            logging.info("URL检查失败")
            return 0



    def  Switch_Map(self):
        '''切换到地图屏'''
        wins = self.session.window_handles
        self.session.switch_to.window(wins[-1])
    def Switch_Service(self):
        '''切换到业务屏'''
        wins = self.session.window_handles
        self.session.switch_to.window(wins[-2])

