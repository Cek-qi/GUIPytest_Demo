# coding=utf-8
import time
from DesignSpace.TestFunction.public.public_debug import *
from DesignSpace.TestFunction.public.public_WaitElement import *

def urlcheck(session, check):
    '''检查url是否符合要求'''
    time.sleep(3)
    logging.info(f"当前URL:{session.current_url}")
    i = 0
    while check not in session.current_url:
        # logging.info(session.current_url)
        time.sleep(1)
        i +=1
        if i > 20:
            return 0
    return 1


