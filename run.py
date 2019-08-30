import os
import time
import logging
import schedule
import configparser
from ybsTwitterUtil import ybsTwitterUtilClass


if __name__ == "__main__":
	# Log
	logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='schedule.log',
                    filemode='a', ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
	logging.info('Schedule starting ...')

	# Config
	Receivers = []
	temps = []
	conf = configparser.ConfigParser()
	conf.read("config.ini")
	for section in conf:
		if 'DEFAULT' not in section:
			user = {}
			user['twitterUsername'] = conf.get(section, 'twitterUsername')
			user['twitterPassword'] = conf.get(section, 'twitterPassword')
			temps.append(user)
	# Set pairs
	users = []
	while len(temps) != 0:
		f = temps[0:1][0]
		n = temps[1:2][0]
		f['Receiver'] = n['twitterUsername']
		users.append(f)
		n['Receiver'] = f['twitterUsername']
		users.append(n)
		temps = temps[2:]

	# Do schedule
	for user in users:
		Receiver = user['Receiver']
		twitterUsername = user['twitterUsername']
		twitterPassword = user['twitterPassword']
		foo = ybsTwitterUtilClass(Receiver, twitterUsername, twitterPassword)
		schedule.every().day.at("08:00").do(foo.run)

	# Blocking model
	while True:
	    schedule.run_pending()
	    time.sleep(60)