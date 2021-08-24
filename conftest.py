# conftest.py文件
# coding:utf-8

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
driver = None


@pytest.fixture(scope='session', autouse=True)
def browser(request):
    global driver
    if driver is None:
        options = Options()
        options.binary_location = r'C:\Users\ycf\AppData\Local\KedaChromium\Application\kedachrome.exe'         #科达浏览器安装路径
        driver = webdriver.Chrome(options=options, executable_path=r'E:\driver\chromedriver.exe')        #driver包路径
    def end():
        #logging.info('测试脚本执行结束')
        driver.quit()                                  #执行结束后关闭浏览器
    request.addfinalizer(end)
    return driver


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'οnclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot():
    '''
    截图保存为base64，展示到html中
    :return:
    '''
    return driver.get_screenshot_as_base64()


