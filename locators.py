from selenium.webdriver.common.by import By

class LoginPageLocators(object):
	USERNAME=(By.ID,'WindowLogin_SimpleForm1_tbxUserName-inputEl')
	PASSWORD=(By.ID,'WindowLogin_SimpleForm1_tbxPassword-inputEl')
	LOGINBTN=(By.ID,'WindowLogin_Toolbar1_btnSure')
	CANCEL=(By.ID,'WindowLogin_Toolbar1_btnCancel')
	ALERT=(By.ID,'messagebox-1001-msg')
	ALERTBTN=(By.ID,'button-1005')
class MainPageLocators(object):
	USER=(By.XPATH,'//*[@id="regions_Region1_ContentPanel1_pnlMiddleLeft_Toolbar1_lblUserNames-inputEl"]/span')
	MAINURL=(By.LINK_TEXT,u'首页')
	TABLINK=(By.ID,'tab-1034')
	SETTINGBTN=(By.ID,'regions_Region1_ContentPanel1_pnlMiddleLeft_Toolbar1_btnLangMenu')
	CANCELBTN=(By.ID,'regions_Region1_ContentPanel1_pnlMiddleLeft_Toolbar1_btnLangMenu_Menu1_btnCancel-itemEl')
class MESPageLocators(object):
	QA=(By.ID,'ext-element-11')
	SORT=(By.ID,'ext-element-40')
	INPUTPROJECT=(By.ID,'ext-element-38')
	LABPROJECT=(By.ID,'ext-element-42')
	TEMPLATE=(By.XPATH,'//*[@id="treeview-1026-record-86"]/tbody/tr/td/div/a')
	LABSHEET=(By.XPATH,'//*[@id="treeview-1026-record-87"]/tbody/tr/td/div/a')
	INPUTDETAIL=(By.ID,'ext-element-44')
	QUERY=(By.ID,'ext-element-47')
	DISPLAY=(By.XPATH,'//*[@id="treeview-1026-record-90"]/tbody/tr/td/div/a')
class CategoryPageLocators(object):
	TITLE=(By.ID,'Panel3_Panel4_dgvItemType_header-title-textEl')
	ADDBTN=(By.ID,'Panel3_Panel4_Toolbar1_btnAdd')
	EDITBTN=(By.ID,'Panel3_Panel4_Toolbar1_btnEdit')
	STOPBTN=(By.ID,'Panel3_Panel4_Toolbar1_btnStop')
	STOPORUSED=(By.ID,'Panel3_Panel4_Toolbar1_btnStop-btnInnerEl')
	VEIWBTN=(By.ID,'Panel3_Panel4_Toolbar1_btnView')
	VEIWTITLE=(By.ID,'TypeConfigWindow_header-title-textEl')
	CATEGORTINPUT=(By.ID,'Panel2_SimpleForm1_txtTypeName-inputEl')
	ORDERINPUT=(By.ID,'Panel2_SimpleForm1_nbOrderFlag-inputEl')
	DESCINPUT=(By.ID,'Panel2_SimpleForm1_txtDescription-inputEl')
	SAVEBTN=(By.ID,'Panel2_Toolbar1_btnSave')
	CLOSEVEIW=(By.ID,'tool-1023')
	MESSAGEBOX=(By.ID,'messagebox-1001-msg')
	MESSAGEBTN=(By.ID,'button-1005')
	TABLEVEIW=(By.ID,'tableview-1022')
	TABLES=(By.TAG_NAME,'table')





