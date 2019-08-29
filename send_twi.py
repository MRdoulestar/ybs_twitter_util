import os,time,random
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Single target
Receiver = 'userid'
twitterUsername=''
twitterPassword=''


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
	twitterBrowser.find_elements_by_class_name('r-3s2u2q')[0].click()
	# find the target
	time.sleep(2)
	twitterBrowser.find_elements_by_class_name('r-30o5oe')[0].send_keys(Receiver)
	# choice target
	time.sleep(5)
	twitterBrowser.find_elements_by_class_name('r-1j63xyz')[0].click()
	# close tab
	time.sleep(1)
	twitterBrowser.find_elements_by_class_name('r-1fneopy')[0].click()

	# Submit
	time.sleep(4)
	twitterBrowser.find_elements_by_class_name('r-1fneopy')[2].click()
	# twitterBrowser.find_element_by_class_name('r-lrvibr').click()

def job():
	print('job working ...  timestamp: ' + str(time.time()))
	try:
		openTwitter()
		time.sleep(4)
		twitterLogin()
		time.sleep(5)
		twitterPost()

		time.sleep(3)
		twitterBrowser.quit()
		print('job end ...')
	except Exception as e:
		print("job error::::")
		print(e)
		twitterBrowser.quit()


if __name__ == "__main__":
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
# print(source)
# print('title:  ' + b.title)
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








