import os,time,random
import logging
import schedule
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Single target
Receiver = 'userid'
twitterUsername='xxx@163.com'
twitterPassword='xxx'


chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# Select one img randomly
def randomImg():
	files = os.listdir(r"./imgs")
	choice_num = random.randint(0, len(files))
	return files[choice_num]

# Init Selenium
def openTwitter():
	twitterUrl='https://twitter.com/login'
	global twitterBrowser
	twitterBrowser=webdriver.Chrome(options=chrome_options)
	twitterBrowser.maximize_window()
	twitterBrowser.get(twitterUrl)
	return twitterBrowser

# User login
def twitterLogin():
	loginEle=twitterBrowser.find_element_by_class_name('js-username-field')
	#loginEle.clear()
	loginEle.send_keys(twitterUsername)
	passwordEle=twitterBrowser.find_element_by_class_name('js-password-field')
	#passwordEle.clear()
	passwordEle.send_keys(twitterPassword)
	twitterBrowser.find_element_by_class_name('EdgeButtom--medium').click()

# Send tweet
def twitterPost():
	# Picture
	picInputEle = twitterBrowser.find_element_by_class_name('r-8akbif')
	# Random pictures
	picName=randomImg()
	picSend=os.path.join(os.getcwd() + '/imgs/' + picName)
	picInputEle.send_keys(picSend)
	time.sleep(2)

	# AT
	twitterBrowser.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div').click()
	ActionChains(twitterBrowser).send_keys(Receiver).perform()
	ActionChains(twitterBrowser).send_keys(Keys.ENTER).perform()
	
	# Tag someone in picture
	# twitterBrowser.find_elements_by_class_name('r-3s2u2q')[0].click()
	# # find the target
	# time.sleep(2)
	# twitterBrowser.find_elements_by_class_name('r-30o5oe')[0].send_keys(Receiver)
	# # choice target
	# time.sleep(5)
	# twitterBrowser.find_elements_by_class_name('r-1j63xyz')[0].click()
	# # close tab
	# time.sleep(1)
	# twitterBrowser.find_elements_by_class_name('r-1fneopy')[0].click()

	# Submit
	time.sleep(3)
	twitterBrowser.find_elements_by_class_name('r-1fneopy')[2].click()

def job():
	logging.info('job working ...  timestamp: ' + str(time.time()))
	try:
		twitterBrowser = openTwitter()
		time.sleep(3)
		twitterLogin()
		time.sleep(4)
		twitterPost()

		time.sleep(3)
		twitterBrowser.quit()
		logging.info('job end ...')
	except Exception as e:
		logging.info("job error::::")
		logging.info(e)
		twitterBrowser.quit()


if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='ybs_twitter_log.log',
                    filemode='a', ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
	logging.info('Schedule starting ...')
	schedule.every().day.at("08:00").do(job)
	while True:
	    schedule.run_pending()
	    time.sleep(60)

# caps = DesiredCapabilities.CHROME
# # caps['loggingPrefs'] = {'performance': 'ALL'}
# chrome_options = Options()

# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

# b = webdriver.Chrome(options=chrome_options, desired_capabilities=caps)
# b.get('http://baidu.com')

# source = b.page_source
# logging.info(source)
# logging.info('title:  ' + b.title)
# #b.close()
# b.quit()



# import tweepy
# consumer_key = 'h1Hm58PCHGVtqy89Yftlp2Idb'
# consumer_secret = 'pSBdos9YGJb4CUXyfDte8uZC1LVSRMxnCQlDDcYCs0hq7fKszM'
# access_token = '1041681094356025344-Ctxo5Zk8QMfHjO9TSwy8eASkEIpcf9'
# access_token_secret = 'tBfRl959HU9hlGOf3QDck1eQ9VaCXLYAwoin84ou7K6lD'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

# tweet = 'Hello, world!'
# api.update_status(status=tweet)








