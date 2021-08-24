# coding=utf-8
# 多维大数据相关页面
# url:tz-e1-management-front/#/
import traceback
import time
from DesignSpace.TestFunction.public.public_debug import *
from DesignSpace.TestFunction.public.public_WaitElement import FindElement
from DesignSpace.TestFunction.public.public_urlcheck import urlcheck
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class DW(FindElement):

    resultall = '//*[@id="kiafLayout"]/div[1]/div[2]/div[3]/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/span'
    resultname = '//*[@id="kiafLayout"]/div[1]/div[2]/div[3]/div/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]'
    resultid = '//*[@id="kiafLayout"]/div[1]/div[2]/div[3]/div/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/span[2]'
    dwdsj = '//*[@id="kiafLayout"]/div[1]/div[1]/div/div/div[2]/div[3]/div[1]'
    #dwdsj = 'kiaf-i-dwdsj'
    YiJianSou = 'kiaf-nav-three-tit'
    searchInput = '//*[@id="searchInput"]'
    search = 'query-icon'
    Car = '//*[@id="kiafLayout"]/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[3]/div[1]/ul/li[2]'

    def __init__(self,session):
        FindElement.__init__(self, session)
        self.session = session


    def Yjs(self):
        time.sleep(2)
        '''点击多维大数据'''
        self.public_WaitElementClass(self.dwdsj)[0].click()
        '''点击打开一键搜页面'''
        self.public_WaitElementClass(self.YiJianSou)[0].click()

    def yjs_search(self,content):
        '''点击搜索'''
        self.public_WaitElementXpath(self.searchInput)[0].send_keys(Keys.BACK_SPACE)  #删除搜索框中内容
        self.public_WaitElementXpath(self.searchInput)[0].send_keys(content)
        time.sleep(1)
        self.public_WaitElementClass(self.search)[0].click()

    def yjs_search_car(self):
        '''切换为车辆'''
        self.public_WaitElementXpath(self.Car)[0].click()
    def search_result_num(self):
        result_all = self.session.find_element_by_xpath(self.resultall).text
        logging.info(result_all)

    def search_result(self,name,ID):
        """人员搜索结果验证"""
        result_name = self.session.find_element_by_xpath(self.resultname).text
        logging.info(result_name)
        assert result_name == name
        result_id = self.session.find_element_by_xpath(self.resultid).text
        logging.info(result_id)
        assert result_id == ID




    def urlEffect(self):
        try:
            urlcheck(self.session, "ezview")
            return 1
        except:
            print(traceback.print_exc())
            logging.info("URL检查失败")
            return 0
    def textcheck(self,text1,text2):
        #Text = self.public_WaitElementXpath(self.text1).text
        if text1 == text2 :
            return 1
        else:
            logging.info('检查失败')
            return 0