#coding=utf-8

class LoginMessage(object):
	EMPTYPASS=u'密码不能为空！'
	FAILPASS=u'密码有误，请重新输入！'
	EMPTYUSER=u'用户名不能为空！'
	FAILUSER=u'该用户不存在！'

class LabMessage(object):
	HEADTITLE='化验项目分类管理'
	ADDSUCCESS=''
	EDITSUCCESS=''
	STOP=u'该化验项目已停用'
	USED=u'该化验项目已启用'