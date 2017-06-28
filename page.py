#coding=utf-8

from base import Page
from locators import *
from time import sleep
class LoginPage(Page):
	def check_page_loaded(self):
		return self.check_element_exists(*LoginPageLocators.USERNAME)

	def enter_username(self,name):
		
		self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(name)
	def clear_username(self):
		self.driver.find_element(*LoginPageLocators.USERNAME).clear()
	def enter_password(self,passwd):
		self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(passwd)
	def clear_password(self):
		self.driver.find_element(*LoginPageLocators.PASSWORD).clear()
	def click_login(self):
		self.driver.find_element(*LoginPageLocators.LOGINBTN).click()
	def login(self,name,passwd):
		self.clear_username()
		sleep(1)
		self.enter_username(name)
		self.clear_password()
		sleep(1)
		self.enter_password(passwd)
		sleep(1)
		self.click_login()
	def get_alter_text(self):
		return self.find_element(*LoginPageLocators.ALERT).text
	def click_alert_btn(self):
		self.find_element(*LoginPageLocators.ALERTBTN).click()
class MainPage(Page):
	def get_user(self):
		return self.find_element(*MainPageLocators.USER).text
	def enter_into_page(self):
		self.find_element(*MainPageLocators.TABLINK).click()
	def cancel(self):
		self.find_element(*MainPageLocators.SETTINGBTN).click()
		sleep(1)
		self.find_element(*MainPageLocators.CANCELBTN).click()

class SortPage(Page):
	def get_into_page(self):
		self.find_element(*MESPageLocators.QA).click()
		sleep(1)
		self.find_element(*MESPageLocators.SORT).click()
		sleep(3)
	def check_page_loaded(self):	
		return self.find_element(*CategoryPageLocators.TITLE).text
	def enter_add(self):
		self.find_element(*CategoryPageLocators.ADDBTN).click()
	def close_veiw(self):
		self.find_element(*CategoryPageLocators.CLOSEVEIW).click()
	def get_add_title(self):
		self.enter_add()
		return self.find_element(*CategoryPageLocators.VEIWTITLE).text
	def enter_category(self,detail):
		self.enter_input(*CategoryPageLocators.CATEGORTINPUT,detail)
	def enter_order(self,num):
		self.enter_input(*CategoryPageLocators.ORDERINPUT,num)
	def enter_detail(self,detail):
		self.enter_input(*CategoryPageLocators.DESCINPUT,detail)
	def enter_save(self):
		self.find_element(*CategoryPageLocators.SAVEBTN).click()
	def get_alter_text(self):
		return self.find_element(*CategoryPageLocators.MESSAGEBOX).text
	def click_alert_btn(self):
		self.find_element(*CategoryPageLocators.MESSAGEBTN).click()
	def get_tables(self):
		tables=self.find_elements(*CategoryPageLocators.TABLEVEIW)
		return tables.find_elements_by_tag_name('table')






		
