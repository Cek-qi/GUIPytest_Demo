import logging
#filename = r'D:\相关文档\自动化\GUIPytest_Demo\ResultSpace\log\my.log'
logging.getLogger().setLevel(logging.INFO)
logging.FileHandler(filename=r'E:\自动化\GUIPytest_Demo\ResultSpace\log\my.log', encoding='utf-8')
logging.basicConfig(level=logging.INFO,filename=r'E:\自动化\GUIPytest_Demo\ResultSpace\log\my.log',
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',filemode='w')



