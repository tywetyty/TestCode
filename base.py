from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class Page(object):
	def __init__(self,driver):
		self.driver=driver
		self.timeout=30
	def find_element(self,*locator):
		return self.driver.find_element(*locator)
	def find_elements(self,*locator):
		return self.driver.find_elements(*locator)
	def get_title(self):
		return self.driver.title
	def get_url(self):
		return self.driver.current_url()
	def hover(self,*locator):
		element=self.find_element(*locator)
		action=ActionChains(self.driver).move_to_element(element)
		action.perform()
	def check_element_exists(self,*locator):
		try:
			self.find_element(*locator)
		except NoSuchElementException:
			return False
		return True
	def checkbox_is_selected(self,*locator):
		return True if(self.find_element(*locator).is_selected()) else False
	def wait_for_element(self,*locator):
		return WebDriverWait(self.driver, self.timeout).until(lambda self:self.find_element(*locator))
	def check_alert_text(self):
		try:
			alert=self.driver.switch_to_alert()
		except NoAlertPresentException:
			return False
		return alert.text
	def click_alert_accept(self):
		alert=self.driver.switch_to_alert()
		alert.accept()
	def enter_input(self,*locator,detail):
		self.find_element(*locator).send_keys(detail)
	def select_by_element_value(self,*locator,value):
		element=self.find_element(*locator)
		select=Select(element)
		select.select_by_value(value)
	def click_double(self,*locator):
		element=self.find_element(*locator)
		ActionChains(self.driver).double_click(element).perform()
	def swith_frame(self,loc):
		return self.driver.switch_to_frame(loc)
	def switch_default_conent(self):
		return self.driver.switch_to_default_conent()






		

		