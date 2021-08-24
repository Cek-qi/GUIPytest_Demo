# coding=utf-8
# 新建模板流程
# ========必选========
import logging

import pytest
import time
from DesignSpace.TestFunction.public.public_debug import *
from DesignSpace.TestFunction.public.public_GetDatas import get_excelDatas
# ========================
from DesignSpace.TestPage.login_Page import loginPage
from DesignSpace.TestPage.DWdsj import DW
from DesignSpace.TestFunction.public.public_WaitElement import FindElement
from DesignSpace.TestFunction.public.public_urlcheck import *



#userID = '320324198402150975'
#searchname = '//*[@id="kiafLayout"]/div[1]/div[2]/div[3]/div/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]'

gd = get_excelDatas()

def test_web(browser):
    global login  # 登录页
    global dw
    global web
    web = browser
    login = loginPage(web)
    dw = DW(web)
    logging.info('打开浏览器')
    web.maximize_window()

@pytest.mark.parametrize("DeviceUrl,UserName,Password",gd.getData("DeviceUrl", "UserName", "Password"))
def test_login(DeviceUrl, UserName, Password):
    '''打开视综页面并登陆'''
    logging.info("loggining")
    login.urlJump(DeviceUrl)
    time.sleep(2)
    login.click_continue()
    time.sleep(10)
    login.input_userName(UserName)
    login.input_passWord(Password)
    login.click_loginButton()
    logging.info("login")
    time.sleep(1)
    assert 1 == login.urlEffect()
    ''''切换到新窗口'''''
    login.Switch_Service()
    time.sleep(3)
    url = web.current_url
    logging.info(url)
    logging.info('切换业务屏')
    time.sleep(1)
    Text = web.find_element_by_xpath('//*[@id="kiafLayout"]/div[1]/div[1]/div/div/div[3]/div[2]/div/span').text
    logging.info(Text)
    assert Text == '地图屏'

@pytest.mark.parametrize("ID",gd.getData('ID'))
def test_search(ID):
    '''人员搜索'''
    dw.Yjs()     # 打开一键搜菜单
    time.sleep(3)
    dw.yjs_search(ID)
    time.sleep(10)
    dw.search_result_num()
    dw.search_result('刘12彬',ID)


@pytest.mark.parametrize("carID",gd.getData('carID'))
def test_search_car(carID):
    '''车辆搜索'''
    dw.Yjs()     # 打开一键搜菜单
    time.sleep(3)
    dw.yjs_search_car()
    dw.yjs_search(carID)
    time.sleep(10)
    dw.search_result_num()
    #dw.search_result('刘彬',cars)




if __name__ == "__main__":
    pytest.main(['-q','test_dw_yjs.py'])