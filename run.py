import os
import time
import logging
import schedule
from ybsTwitterUtil import ybsTwitterUtilClass


if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='schedule.log',
                    filemode='a', ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
	logging.info('Schedule starting ...')
	t = ybsTwitterUtilClass()
	schedule.every().day.at("08:00").do(t.run)
	while True:
	    schedule.run_pending()
	    time.sleep(60)