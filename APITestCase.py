import requests
import unittest
from time import sleep
BASE_URL='http://10.10.10.46:8066'
class APILimsTest(unittest.TestCase):
	def __init__(self,*args,**kwargs):
		super(APILimsTest,self).__init__(*args,*kwargs)
		self._api_base_url=BASE_URL+'/api/Lims'
	def test_GetTestItemList(self):
		url='/GetTestItemList'
		params={'reportID':'TP2017052'}
		r=requests.get(self._api_base_url+url,params=params)
		result=r.json()
		self.assertEqual(result['data'][0]['TestItemName'], u'顶部')
		self.assertEqual(len(result['data']), 1)
	def test_InsertTestItemType(self):
		url='/InsertTestItemType'
		data={
			# 'TestItemTypeID':'TP201706211029',
			'TestItemTypeName':'TestItem001',
			'IsUsed':True,
			'OrderFlag':9,
			'Description':'TestItem001'
		}
		r=requests.post(self._api_base_url+url,data=data)
		result=r.json()
		self.assertTrue(result['data'])
	
		