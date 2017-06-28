from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import unittest
import os



class AppTest(unittest.TestCase):
	"""docstring for AppTest"""
	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '4.4.2'
		desired_caps['deviceName'] = 'f82bfa17'
		desired_caps['app'] = 'D:/BI/Asynchronous/WebTest/apps/ApiDemos-debug.apk'
		self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
	def tearDown(self):
		self.driver.quit()
	def check_element_extis(self,name):
		try:
			self.driver.find_element_by_accessibility_id(name)
			
		except NoSuchElementException:
			return False
		return True

	def test_Animatton(self):
		el = self.driver.find_element_by_accessibility_id('Animation')
		self.assertTrue(self.check_element_extis('Animation'))
		el.click()

if __name__ == '__main__':
	unittest.main()