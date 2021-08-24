# coding=utf-8
# 元素定位
import traceback
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class FindElement():
    def __init__(self,session):
        self.session = session

    def public_WaitElementTag(self,tag, timeout=5, OtherBase=""):
        '''抓取元素按照tag
        session:本次session
        tag: 标签类型
        timeout:超时时间'''
        menu = []
        try:
            if OtherBase:
                menu = WebDriverWait(driver=OtherBase, timeout=timeout).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, tag)))
            else:
                menu = WebDriverWait(driver=self.session, timeout=timeout).until(
                    EC.presence_of_all_elements_located((By.TAG_NAME, tag)))
        except:
            print(traceback.print_exc())
        return menu

    def public_WaitElementClass(self, className, timeout=5, OtherBase=""):
        '''抓取元素按照tclassName
        session:本次session
        xpath: xpath地址
        timeout:超时时间'''
        menu = []
        try:
            if OtherBase:
                menu = WebDriverWait(driver=OtherBase, timeout=timeout).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, className)))
            else:
                menu = WebDriverWait(driver=self.session, timeout=timeout).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, className)))
        except:
            print(traceback.print_exc())
        return menu

    def public_WaitElementXpath(self, xpath, timeout=5, OtherBase=""):
        '''
        按照xpath定位元素
        session:本次session
        xpath: xpath地址
        timeout:超时时间
        '''
        menu = []
        try:
            if OtherBase:
                menu = WebDriverWait(driver=OtherBase, timeout=timeout).until(
                    EC.presence_of_all_elements_located((By.XPATH, xpath)))
            else:
                menu = WebDriverWait(driver=self.session, timeout=timeout).until(
                    EC.presence_of_all_elements_located((By.XPATH, xpath)))
        except:
            print(traceback.print_exc())

        return menu
