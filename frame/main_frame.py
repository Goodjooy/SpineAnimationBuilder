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

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 512,512 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
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

		self.m_staticline20 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer8.Add( self.m_staticline20, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button6, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button7, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer9.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"工作的事件", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer9.Add( self.m_staticText18, 0, wx.ALL, 5 )

		m_listBox2Choices = []
		self.m_listBox2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, 0 )
		bSizer9.Add( self.m_listBox2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer8.Add( bSizer9, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_checkList2.Bind( wx.EVT_LISTBOX_DCLICK, self.edit_event )
		self.m_checkList2.Bind( wx.EVT_CHECKLISTBOX, self.set_to_work )
		self.m_button6.Bind( wx.EVT_BUTTON, self.add_behave )
		self.m_button7.Bind( wx.EVT_BUTTON, self.del_behave )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def edit_event( self, event ):
		event.Skip()

	def set_to_work( self, event ):
		event.Skip()

	def add_behave( self, event ):
		event.Skip()

	def del_behave( self, event ):
		event.Skip()


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

		self.m_staticline17 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline17, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"帧率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer11.Add( self.m_staticText17, 0, wx.ALL, 5 )

		m_comboBox3Choices = [ u"30", u"60" ]
		self.m_comboBox3 = wx.ComboBox( self, wx.ID_ANY, u"30", wx.DefaultPosition, wx.DefaultSize, m_comboBox3Choices, 0 )
		self.m_comboBox3.SetSelection( 0 )
		bSizer11.Add( self.m_comboBox3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline18 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline18, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"背景颜色", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer11.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.m_colourPicker_bg = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 0, 255, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_USE_TEXTCTRL )
		bSizer11.Add( self.m_colourPicker_bg, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline19 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer11.Add( self.m_staticline19, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_button_new_work = wx.Button( self, wx.ID_ANY, u"新建-工作区", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button_new_work, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()
		bSizer11.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button_new_work.Bind( wx.EVT_BUTTON, self.creat_workshop )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def creat_workshop( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog_event
###########################################################################

class MyDialog_event ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 317,577 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"进行活动的模块", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		bSizer23.Add( self.m_staticText19, 0, wx.ALL, 5 )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		bSizer23.Add( self.m_choice3, 0, wx.ALL, 5 )


		bSizer22.Add( bSizer23, 1, wx.EXPAND, 5 )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"持续不断（一直到其他动作结束）", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"到达后以相同的速度返回", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.m_checkBox4 = wx.CheckBox( self, wx.ID_ANY, u"后续的部件一同旋转", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_checkBox4, 0, wx.ALL, 5 )

		m_radioBox3Choices = [ u"绕中心点旋转", u"绕关节旋转" ]
		self.m_radioBox3 = wx.RadioBox( self, wx.ID_ANY, u"旋转方式", wx.DefaultPosition, wx.DefaultSize, m_radioBox3Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox3.SetSelection( 0 )
		bSizer24.Add( self.m_radioBox3, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer22.Add( bSizer24, 0, wx.EXPAND, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"旋转" ), wx.HORIZONTAL )

		self.m_button11 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"旋转角度", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_button11, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		sbSizer1.Add( self.m_spinCtrl2, 0, wx.ALL, 5 )


		bSizer22.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"持续时间" ), wx.HORIZONTAL )

		self.m_spinCtrl3 = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, u"0.1", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 10 )
		sbSizer2.Add( self.m_spinCtrl3, 0, wx.ALL, 5 )

		self.m_spinCtrlDouble1 = wx.SpinCtrlDouble( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0, 1 )
		self.m_spinCtrlDouble1.SetDigits( 0 )
		sbSizer2.Add( self.m_spinCtrlDouble1, 0, wx.ALL, 5 )


		bSizer22.Add( sbSizer2, 1, wx.EXPAND, 5 )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"相对固定体的位移" ), wx.HORIZONTAL )

		self.m_staticText20 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"x:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		sbSizer3.Add( self.m_staticText20, 1, wx.ALL, 5 )

		self.m_spinCtrl6 = wx.SpinCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 1 )
		sbSizer3.Add( self.m_spinCtrl6, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline24 = wx.StaticLine( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer3.Add( self.m_staticline24, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"y:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		sbSizer3.Add( self.m_staticText21, 1, wx.ALL, 5 )

		self.m_spinCtrl7 = wx.SpinCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 1000, 0 )
		sbSizer3.Add( self.m_spinCtrl7, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer22.Add( sbSizer3, 1, wx.EXPAND, 5 )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"设置绘制顺序" ), wx.HORIZONTAL )

		self.m_textCtrl3 = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_spinBtn1 = wx.SpinButton( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_spinBtn1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline23 = wx.StaticLine( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		sbSizer4.Add( self.m_staticline23, 0, wx.EXPAND |wx.ALL, 5 )

		m_choice4Choices = []
		self.m_choice4 = wx.Choice( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		sbSizer4.Add( self.m_choice4, 0, wx.ALL, 5 )


		bSizer22.Add( sbSizer4, 1, wx.EXPAND, 5 )

		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
		self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
		m_sdbSizer2.Realize();

		bSizer22.Add( m_sdbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer22 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


