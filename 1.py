#coding=utf-8
import os
os.environ['KIVY_TEXT']='pil'
os.environ['KIVY_NO_ARGS']='1'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ListProperty
class LoginScreen(BoxLayout):
	"""docstring for LoginScreen"""
	def __init__(self, **kwargs):
		super(LoginScreen, self).__init__(**kwargs)
		self.add_widget(Button(text='btn 1'))
		cb=CustomBtn()
		cb.bind(pressed=self.btn_pressed)
		self.add_widget(cb)
		self.add_widget(Button(text='btn 2'))
	def btn_pressed(self,instance,pos):
		print('pos:printed from root widget:{pos}'.format(pos=pos))
class CustomBtn(Widget):
	pressed	=	ListProperty([0,	0])
	def	on_touch_down(self,	touch):
		if	self.collide_point(*touch.pos):
			self.pressed=touch.pos
			return	True
		return	super(CustomBtn,	self).on_touch_down(touch)
	def	on_pressed(self,	instance,	pos):
		print	('pressed	at	{pos}'.format(pos=pos))		

class MyApp(App):
	def build(self):
		return LoginScreen()
		
if __name__ == '__main__':
	MyApp().run()