import os,time,random
import logging
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class ybsTwitterUtilClass:
	def __init__(self, Receiver, twitterUsername, twitterPassword):
		self.Receiver = Receiver
		self.twitterUsername = twitterUsername
		self.twitterPassword = twitterPassword
		self.chrome_options = Options()
		# chrome_options.add_argument('--headless')
		self.chrome_options.add_argument('--disable-gpu')
		self.twitterBrowser = None

	# Select one img randomly
	def randomImg(self):
		files = os.listdir(r"./imgs")
		choice_num = random.randint(0, len(files))
		return files[choice_num]

	# Init Selenium
	def openTwitter(self):
		twitterUrl='https://twitter.com/login'
		self.twitterBrowser=webdriver.Chrome(options=self.chrome_options)
		# twitterBrowser.maximize_window()
		self.twitterBrowser.get(twitterUrl)

	# User login
	def twitterLogin(self):
		loginEle=self.twitterBrowser.find_element_by_class_name('js-username-field')
		#loginEle.clear()
		loginEle.send_keys(self.twitterUsername)
		passwordEle=self.twitterBrowser.find_element_by_class_name('js-password-field')
		#passwordEle.clear()
		passwordEle.send_keys(self.twitterPassword)
		self.twitterBrowser.find_element_by_class_name('EdgeButtom--medium').click()

	# Send tweet
	def twitterPost(self):
		# Picture
		picInputEle = self.twitterBrowser.find_element_by_class_name('r-8akbif')
		# Random pictures
		picName = self.randomImg()
		picSend = os.path.join(os.getcwd() + '/imgs/' + picName)
		picInputEle.send_keys(picSend)
		time.sleep(2)

		# AT
		self.twitterBrowser.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div').click()
		ActionChains(self.twitterBrowser).send_keys(self.Receiver).perform()
		ActionChains(self.twitterBrowser).send_keys(Keys.ENTER).perform()
		
		# Tag someone in picture
		# self.twitterBrowser.find_elements_by_class_name('r-3s2u2q')[0].click()
		# # find the target
		# time.sleep(2)
		# self.twitterBrowser.find_elements_by_class_name('r-30o5oe')[0].send_keys(Receiver)
		# # choice target
		# time.sleep(5)
		# self.twitterBrowser.find_elements_by_class_name('r-1j63xyz')[0].click()
		# # close tab
		# time.sleep(1)
		# self.twitterBrowser.find_elements_by_class_name('r-1fneopy')[0].click()

		# Submit
		time.sleep(3)
		self.twitterBrowser.find_elements_by_class_name('r-1fneopy')[2].click()

	def run(self):
		logging.info('Running...  timestamp: ' + str(time.time()))
		try:
			self.openTwitter()
			time.sleep(3)
			self.twitterLogin()
			time.sleep(4)
			self.twitterPost()
			time.sleep(3)
			self.twitterBrowser.quit()
			logging.info('End ...')
		except Exception as e:
			logging.info("Job error::::")
			logging.info(e)
			self.twitterBrowser.quit()


if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO,#控制台打印的日志级别
                    # filename='ybs_twitter_log.log',
                    # filemode='a', ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
	t = ybsTwitterUtilClass()
	t.run()









