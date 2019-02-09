# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"spine动画小人制作工具", pos = wx.DefaultPosition, size = wx.Size( 360,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		m_radioBox_in_typeChoices = [ u"从贴图-分割文件导入", u"从已有的文件导入" ]
		self.m_radioBox_in_type = wx.RadioBox( self, wx.ID_ANY, u"导入方式", wx.DefaultPosition, wx.DefaultSize, m_radioBox_in_typeChoices, 2, wx.RA_SPECIFY_ROWS )
		self.m_radioBox_in_type.SetSelection( 1 )
		bSizer2.Add( self.m_radioBox_in_type, 0, wx.ALL, 5 )

		self.m_simplebook1 = wx.Simplebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_from_tex = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_filePicker_tex = wx.FilePickerCtrl( self.m_panel_from_tex, wx.ID_ANY, wx.EmptyString, u"选择贴图文件", u"*.png", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_SMALL )
		bSizer3.Add( self.m_filePicker_tex, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_filePicker_txt = wx.FilePickerCtrl( self.m_panel_from_tex, wx.ID_ANY, wx.EmptyString, u"选择分割文件", u"*.atlas.txt", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_SMALL )
		bSizer3.Add( self.m_filePicker_txt, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_from_tex.SetSizer( bSizer3 )
		self.m_panel_from_tex.Layout()
		bSizer3.Fit( self.m_panel_from_tex )
		self.m_simplebook1.AddPage( self.m_panel_from_tex, u"a page", False )
		self.m_panel_from_file = wx.Panel( self.m_simplebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_filePicker_work = wx.FilePickerCtrl( self.m_panel_from_file, wx.ID_ANY, wx.EmptyString, u"spine小人动画制作工程文件-测试", u"*.sp.json", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_SMALL )
		bSizer4.Add( self.m_filePicker_work, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel_from_file.SetSizer( bSizer4 )
		self.m_panel_from_file.Layout()
		bSizer4.Fit( self.m_panel_from_file )
		self.m_simplebook1.AddPage( self.m_panel_from_file, u"a page", False )

		bSizer2.Add( self.m_simplebook1, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"子零件", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1.Wrap( -1 )

		bSizer5.Add( self.m_staticText1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		m_listBox_submodelChoices = []
		self.m_listBox_submodel = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox_submodelChoices, wx.LB_ALWAYS_SB|wx.LB_HSCROLL|wx.LB_SINGLE )
		bSizer5.Add( self.m_listBox_submodel, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"关节连接", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button4, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"绘制顺序", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText2.Wrap( -1 )

		bSizer6.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		gSizer2 = wx.GridSizer( 0, 4, 0, 0 )

		self.m_bpButton_to_first = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_to_first.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GOTO_FIRST, wx.ART_BUTTON ) )
		gSizer2.Add( self.m_bpButton_to_first, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_bpButton_up = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_up.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ) )
		gSizer2.Add( self.m_bpButton_up, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_bpButton_down = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_down.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_FORWARD, wx.ART_BUTTON ) )
		gSizer2.Add( self.m_bpButton_down, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_bpButton_to_end = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton_to_end.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GOTO_LAST, wx.ART_BUTTON ) )
		gSizer2.Add( self.m_bpButton_to_end, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer6.Add( gSizer2, 0, wx.EXPAND, 5 )

		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )

		m_checkList_drawChoices = []
		self.m_checkList_draw = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList_drawChoices, wx.LB_ALWAYS_SB|wx.LB_EXTENDED|wx.LB_HSCROLL )
		bSizer6.Add( self.m_checkList_draw, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"消除选择", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button5, 0, wx.ALL|wx.EXPAND, 5 )


		gSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )


		bSizer1.Add( gSizer1, 1, wx.EXPAND, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"渲染进度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_gauge_work = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge_work.SetValue( 0 )
		bSizer1.Add( self.m_gauge_work, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button_save = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button_save, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer7.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_toggleBtn_time_line = wx.ToggleButton( self, wx.ID_ANY, u"时间轴", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_toggleBtn_time_line, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer7.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button_help = wx.Button( self, wx.ID_ANY, u"帮助", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button_help, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer7, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_radioBox_in_type.Bind( wx.EVT_RADIOBOX, self.change_in )
		self.m_filePicker_tex.Bind( wx.EVT_FILEPICKER_CHANGED, self.get_tex_file )
		self.m_filePicker_txt.Bind( wx.EVT_FILEPICKER_CHANGED, self.get_div_file )
		self.m_filePicker_work.Bind( wx.EVT_FILEPICKER_CHANGED, self.get_work_file )
		self.m_listBox_submodel.Bind( wx.EVT_LISTBOX, self.view_model )
		self.m_listBox_submodel.Bind( wx.EVT_LISTBOX_DCLICK, self.edit_model )
		self.m_button4.Bind( wx.EVT_BUTTON, self.link )
		self.m_bpButton_to_first.Bind( wx.EVT_BUTTON, self.to_first )
		self.m_bpButton_up.Bind( wx.EVT_BUTTON, self.to_up )
		self.m_bpButton_down.Bind( wx.EVT_BUTTON, self.to_down )
		self.m_bpButton_to_end.Bind( wx.EVT_BUTTON, self.to_end )
		self.m_checkList_draw.Bind( wx.EVT_LISTBOX, self.view_mod )
		self.m_checkList_draw.Bind( wx.EVT_LISTBOX_DCLICK, self.edit_mod )
		self.m_checkList_draw.Bind( wx.EVT_CHECKLISTBOX, self.set_view )
		self.m_button5.Bind( wx.EVT_BUTTON, self.clear_select )
		self.m_button_save.Bind( wx.EVT_BUTTON, self.save_work )
		self.m_toggleBtn_time_line.Bind( wx.EVT_TOGGLEBUTTON, self.time_line )
		self.m_button_help.Bind( wx.EVT_BUTTON, self.help )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def change_in( self, event ):
		event.Skip()

	def get_tex_file( self, event ):
		event.Skip()

	def get_div_file( self, event ):
		event.Skip()

	def get_work_file( self, event ):
		event.Skip()

	def view_model( self, event ):
		event.Skip()

	def edit_model( self, event ):
		event.Skip()

	def link( self, event ):
		event.Skip()

	def to_first( self, event ):
		event.Skip()

	def to_up( self, event ):
		event.Skip()

	def to_down( self, event ):
		event.Skip()

	def to_end( self, event ):
		event.Skip()

	def view_mod( self, event ):
		event.Skip()

	def edit_mod( self, event ):
		event.Skip()

	def set_view( self, event ):
		event.Skip()

	def clear_select( self, event ):
		event.Skip()

	def save_work( self, event ):
		event.Skip()

	def time_line( self, event ):
		event.Skip()

	def help( self, event ):
		event.Skip()


###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,400 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_bitmap1, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"事件集", pos = wx.DefaultPosition, size = wx.Size( 394,336 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		m_checkList2Choices = []
		self.m_checkList2 = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList2Choices, 0 )
		bSizer8.Add( self.m_checkList2, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button7, 0, wx.ALL, 5 )


		bSizer8.Add( bSizer9, 0, 0, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyDialog_set_link
###########################################################################

class MyDialog_set_link ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"设置连接", pos = wx.DefaultPosition, size = wx.Size( 308,319 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText_mod = wx.StaticText( self, wx.ID_ANY, u"部件：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_mod.Wrap( -1 )

		bSizer12.Add( self.m_staticText_mod, 0, wx.ALL, 5 )

		self.m_staticline9 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer12.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"连接于：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer14.Add( self.m_staticText9, 1, wx.ALL, 5 )

		m_choice_linksChoices = [ u"固定" ]
		self.m_choice_links = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_linksChoices, 0 )
		self.m_choice_links.SetSelection( 0 )
		bSizer14.Add( self.m_choice_links, 1, wx.ALL, 5 )


		bSizer12.Add( bSizer14, 1, wx.EXPAND, 5 )

		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer12.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"连接坐标点", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer15.Add( self.m_staticText10, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_selet = wx.Button( self, wx.ID_ANY, u"手动选择", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_button_selet, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText_pos = wx.StaticText( self, wx.ID_ANY, u"x:\ny:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_pos.Wrap( -1 )

		bSizer15.Add( self.m_staticText_pos, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer12.Add( bSizer15, 1, wx.EXPAND, 5 )

		self.m_staticline111 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer12.Add( self.m_staticline111, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"连接目标坐标点", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		bSizer151.Add( self.m_staticText101, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_selet_to = wx.Button( self, wx.ID_ANY, u"手动选择", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer151.Add( self.m_button_selet_to, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText_pos_to = wx.StaticText( self, wx.ID_ANY, u"x:\ny:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_pos_to.Wrap( -1 )

		bSizer151.Add( self.m_staticText_pos_to, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer12.Add( bSizer151, 1, wx.EXPAND, 5 )

		self.m_staticline15 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer12.Add( self.m_staticline15, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_colourPicker_bg_picker = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 255, 255, 255 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL )
		bSizer12.Add( self.m_colourPicker_bg_picker, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline16 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer12.Add( self.m_staticline16, 0, wx.EXPAND |wx.ALL, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer12.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_choice_links.Bind( wx.EVT_CHOICE, self.link_work )
		self.m_button_selet.Bind( wx.EVT_BUTTON, self.select_be_linked )
		self.m_button_selet_to.Bind( wx.EVT_BUTTON, self.select_link )
		self.m_colourPicker_bg_picker.Bind( wx.EVT_COLOURPICKER_CHANGED, self.change_bg )
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.cancel_work )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.ok_work )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def link_work( self, event ):
		event.Skip()

	def select_be_linked( self, event ):
		event.Skip()

	def select_link( self, event ):
		event.Skip()

	def change_bg( self, event ):
		event.Skip()

	def cancel_work( self, event ):
		event.Skip()

	def ok_work( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog_size
###########################################################################

class MyDialog_size ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"新建工作区", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"宽", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer11.Add( self.m_staticText4, 0, wx.ALL, 5 )

		m_comboBox_widthChoices = [ u"1080", u"360", u"512" ]
		self.m_comboBox_width = wx.ComboBox( self, wx.ID_ANY, u"1080", wx.DefaultPosition, wx.DefaultSize, m_comboBox_widthChoices, 0 )
		self.m_comboBox_width.SetSelection( 0 )
		bSizer11.Add( self.m_comboBox_width, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"长", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer11.Add( self.m_staticText5, 0, wx.ALL, 5 )

		m_comboBox_heightChoices = [ u"512", u"720", u"1920" ]
		self.m_comboBox_height = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_heightChoices, wx.CB_SORT )
		self.m_comboBox_height.SetSelection( 0 )
		bSizer11.Add( self.m_comboBox_height, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"背景颜色", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer11.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_colourPicker_bg = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 0, 255, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_USE_TEXTCTRL )
		bSizer11.Add( self.m_colourPicker_bg, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button_new_work = wx.Button( self, wx.ID_ANY, u"新建-工作区", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button_new_work, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()
		bSizer11.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


