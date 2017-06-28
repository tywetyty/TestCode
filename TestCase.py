#coding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
from page import *
import unittest
from time import sleep
from AlertMessage import *
BASE_URL='http://localhost:28215/Login.aspx'
class TestLoginPages(unittest.TestCase):
	u'''登录页面测试'''
	def setUp(self):
		self.driver=webdriver.Ie()
		self.driver.maximize_window()
		self.driver.get(BASE_URL)
	def test_empty_pass(self):
		u'''测试不输入任何密码'''
		page=LoginPage(self.driver)
		page.clear_username()
		page.enter_username('admin')
		page.clear_password()
		page.click_login()
		self.driver.implicitly_wait(4)
		self.assertEqual(page.get_alter_text(), LoginMessage.EMPTYPASS)
		page.click_alert_btn()
		self.driver.implicitly_wait(5)
	def test_fail_pass(self):
		u'''测试输入错误的密码'''
		page=LoginPage(self.driver)
		page.clear_username()
		page.enter_username('admin')
		page.clear_password()
		page.enter_password('111')
		page.click_login()
		self.driver.implicitly_wait(5)
		self.assertEqual(page.get_alter_text(), LoginMessage.FAILPASS)
		self.driver.implicitly_wait(5)
		page.click_alert_btn()
		self.driver.implicitly_wait(5)
	def test_empty_username(self):
		u'''测试不输入用户名'''
		page=LoginPage(self.driver)
		page.clear_username()
		page.clear_password()
		page.click_login()
		self.driver.implicitly_wait(4)
		self.assertEqual(page.get_alter_text(), LoginMessage.EMPTYUSER)
		sleep(1)
		page.click_alert_btn()
		self.driver.implicitly_wait(5)
	def test_fail_username(self):
		u'''测试输入输入用户名不存在'''
		page=LoginPage(self.driver)
		sleep(1)
		page.clear_username()
		page.enter_username('www')
		sleep(1)
		page.click_login()
		self.driver.implicitly_wait(4)
		self.assertEqual(page.get_alter_text(), LoginMessage.FAILUSER)
		self.driver.implicitly_wait(5)
		page.click_alert_btn()
		self.driver.implicitly_wait(5)
	def test_login_success(self):
		u'''登录成功'''
		page=LoginPage(self.driver)
		page.login('admin', 'admin')
		self.driver.implicitly_wait(5)
		mainpage=MainPage(self.driver)
		self.assertEqual(mainpage.get_user(), 'admin')
		self.driver.implicitly_wait(5)
		mainpage.cancel()
	def tearDown(self):
		self.driver.quit()

class TestSortPage(unittest.TestCase):
	u'''化验项目分类管理'''
	def setUp(self):
		self.driver=webdriver.Ie()
		self.driver.maximize_window()
		self.driver.get(BASE_URL)
		self.driver.implicitly_wait(3)
		page=LoginPage(self.driver)
		page.login('admin', 'admin')
		self.driver.implicitly_wait(5)
		storpage=SortPage(self.driver)
		storpage.get_into_page()
		self.driver.implicitly_wait(4)
	def test_page_loaded(self):		
		page=SortPage(self.driver)
		self.assertEqual(page.check_page_loaded(), )
		self.driver.implicitly_wait(3)

	def tearDown(self):
		self.driver.quit()