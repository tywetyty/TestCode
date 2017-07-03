#import unittest
import HTMLTestRunner
from APITestCase import *
from TestCase import *
import time
import argparse
import sys
import threading 

def run_api_test():
	print('--------------Start API Test-------------------')
	apisuite=unittest.TestLoader().loadTestsFromTestCase(APILimsTest)
	apireport='./report/APIReport'+time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()))+'.html'
	apifp=open(apireport,'wb')
	apirunner=HTMLTestRunner.HTMLTestRunner(
		stream=apifp,
		title=u'API测试报告',
		description=u'测试结果'
		)
	apirunner.run(apisuite)
	print('--------------End API Test-------------------')

def run_ui_test():
	print('--------------Start UI Test-------------------')
	suite=unittest.TestLoader().loadTestsFromTestCase(TestSortPages)
	report='./report/Report'+time.strftime('_%Y%m%d_%H%M%S',time.localtime(time.time()))+'.html'
	fp=open(report,'wb')
	runner=HTMLTestRunner.HTMLTestRunner(
		stream=fp,
		title=u'测试报告',
		description=u'测试结果')
	runner.run(suite)
	print('--------------End UI Test-------------------')

if __name__ == '__main__':
	# parser=argparse.ArgumentParser()
	# parser.add_argument('-run',help='Run Test!')
	# arg=parser.parse_args()
	# if arg.run=='api' or arg.run=='API':
	# 	run_api_test()
	# elif arg.run=='UI' or arg.run=='ui':
	# 	run_ui_test()
	# else:
	# 	api=threading.Thread(target=run_api_test)
	# 	ui=threading.Thread(target=run_ui_test)
	# 	api.start()
	# 	ui.start()
	run_ui_test()
	