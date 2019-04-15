# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.dataview
import wx.propgrid as pg

###########################################################################
## Class DataStudioUI
###########################################################################

class DataStudioUI ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"DataStudio", pos = wx.DefaultPosition, size = wx.Size( 1091,684 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.file = wx.Menu()
		self.m_menubar1.Append( self.file, u"File" )

		self.edit = wx.Menu()
		self.m_menubar1.Append( self.edit, u"Edit" )

		self.view = wx.Menu()
		self.m_menubar1.Append( self.view, u"View" )

		self.tool = wx.Menu()
		self.m_menubar1.Append( self.tool, u"Tool" )

		self.help = wx.Menu()
		self.m_menubar1.Append( self.help, u"Help" )

		self.SetMenuBar( self.m_menubar1 )

		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.m_toolBar1.Realize()

		gSizer1 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_splitter2 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 3,-1 ), wx.SP_3D|wx.SP_3DBORDER|wx.SP_3DSASH|wx.SP_BORDER|wx.SP_LIVE_UPDATE|wx.SP_PERMIT_UNSPLIT|wx.SP_THIN_SASH )
		self.m_splitter2.SetSashSize( 3 )
		self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )

		self.m_panel5 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_notebook3 = wx.Notebook( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_BOTTOM )
		self.m_panel161 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_treeCtrl1 = wx.TreeCtrl( self.m_panel161, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE, wx.DefaultValidator, u"terterter" )
		self.m_treeCtrl1.SetToolTip( u"ttttttt" )

		bSizer14.Add( self.m_treeCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel161.SetSizer( bSizer14 )
		self.m_panel161.Layout()
		bSizer14.Fit( self.m_panel161 )
		self.m_notebook3.AddPage( self.m_panel161, u"服务器", False )
		self.m_panel17 = wx.Panel( self.m_notebook3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_treeCtrl2 = wx.TreeCtrl( self.m_panel17, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer16.Add( self.m_treeCtrl2, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel17.SetSizer( bSizer16 )
		self.m_panel17.Layout()
		bSizer16.Fit( self.m_panel17 )
		self.m_notebook3.AddPage( self.m_panel17, u"文件", True )

		gSizer3.Add( self.m_notebook3, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel5.SetSizer( gSizer3 )
		self.m_panel5.Layout()
		gSizer3.Fit( self.m_panel5 )
		self.m_panel1 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_notebook4 = wx.Notebook( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel9 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter3 = wx.SplitterWindow( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_3DBORDER|wx.SP_LIVE_UPDATE )
		self.m_splitter3.Bind( wx.EVT_IDLE, self.m_splitter3OnIdle )

		self.m_panel10 = wx.Panel( self.m_splitter3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		# WARNING: wxPython code generation isn't supported for this widget yet.
		self.m_scintilla2 = wx.Window( self.m_panel10 )
		bSizer4.Add( self.m_scintilla2, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel10.SetSizer( bSizer4 )
		self.m_panel10.Layout()
		bSizer4.Fit( self.m_panel10 )
		self.m_panel12 = wx.Panel( self.m_splitter3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook5 = wx.Notebook( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_BOTTOM )
		self.m_panel13 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid2 = wx.grid.Grid( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid2.CreateGrid( 5, 5 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( True )
		self.m_grid2.SetMargins( 0, 0 )

		# Columns
		self.m_grid2.EnableDragColMove( True )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelValue( 0, u"test" )
		self.m_grid2.SetColLabelValue( 1, u"test" )
		self.m_grid2.SetColLabelValue( 2, u"test" )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelValue( 0, u"teter" )
		self.m_grid2.SetRowLabelValue( 1, u"ertre" )
		self.m_grid2.SetRowLabelValue( 2, u"ete" )
		self.m_grid2.SetRowLabelValue( 3, u"t" )
		self.m_grid2.SetRowLabelValue( 4, u"er" )
		self.m_grid2.SetRowLabelValue( 5, u"t" )
		self.m_grid2.SetRowLabelValue( 6, wx.EmptyString )
		self.m_grid2.SetRowLabelValue( 7, wx.EmptyString )
		self.m_grid2.SetRowLabelValue( 8, wx.EmptyString )
		self.m_grid2.SetRowLabelValue( 9, wx.EmptyString )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer9.Add( self.m_grid2, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel13.SetSizer( bSizer9 )
		self.m_panel13.Layout()
		bSizer9.Fit( self.m_panel13 )
		self.m_notebook5.AddPage( self.m_panel13, u"网格", False )
		self.m_panel14 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_dataViewListCtrl1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel15 = wx.Panel( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel14.SetSizer( bSizer11 )
		self.m_panel14.Layout()
		bSizer11.Fit( self.m_panel14 )
		self.m_notebook5.AddPage( self.m_panel14, u"客户端统计", False )
		self.m_panel16 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_propertyGrid1 = pg.PropertyGrid(self.m_panel16, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_DEFAULT_STYLE)
		self.m_propertyGridItem1 = self.m_propertyGrid1.Append( pg.StringProperty( u"Name", u"Name" ) )
		bSizer13.Add( self.m_propertyGrid1, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel16.SetSizer( bSizer13 )
		self.m_panel16.Layout()
		bSizer13.Fit( self.m_panel16 )
		self.m_notebook5.AddPage( self.m_panel16, u"消息", False )

		bSizer7.Add( self.m_notebook5, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel12.SetSizer( bSizer7 )
		self.m_panel12.Layout()
		bSizer7.Fit( self.m_panel12 )
		self.m_splitter3.SplitHorizontally( self.m_panel10, self.m_panel12, 300 )
		bSizer2.Add( self.m_splitter3, 1, wx.EXPAND, 3 )


		self.m_panel9.SetSizer( bSizer2 )
		self.m_panel9.Layout()
		bSizer2.Fit( self.m_panel9 )
		self.m_notebook4.AddPage( self.m_panel9, u"pg.sql", False )
		self.m_panel11 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter31 = wx.SplitterWindow( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter31.Bind( wx.EVT_IDLE, self.m_splitter31OnIdle )

		self.m_panel101 = wx.Panel( self.m_splitter31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		# WARNING: wxPython code generation isn't supported for this widget yet.
		self.m_scintilla21 = wx.Window( self.m_panel101 )
		bSizer41.Add( self.m_scintilla21, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel101.SetSizer( bSizer41 )
		self.m_panel101.Layout()
		bSizer41.Fit( self.m_panel101 )
		self.m_panel121 = wx.Panel( self.m_splitter31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer71 = wx.BoxSizer( wx.VERTICAL )


		self.m_panel121.SetSizer( bSizer71 )
		self.m_panel121.Layout()
		bSizer71.Fit( self.m_panel121 )
		self.m_splitter31.SplitHorizontally( self.m_panel101, self.m_panel121, 300 )
		bSizer21.Add( self.m_splitter31, 1, wx.EXPAND, 3 )


		self.m_panel11.SetSizer( bSizer21 )
		self.m_panel11.Layout()
		bSizer21.Fit( self.m_panel11 )
		self.m_notebook4.AddPage( self.m_panel11, u"ora.sql", False )
		self.m_panel26 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		bSizer211 = wx.BoxSizer( wx.VERTICAL )

		self.m_splitter311 = wx.SplitterWindow( self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter311.Bind( wx.EVT_IDLE, self.m_splitter311OnIdle )

		self.m_panel1011 = wx.Panel( self.m_splitter311, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer411 = wx.BoxSizer( wx.VERTICAL )

		# WARNING: wxPython code generation isn't supported for this widget yet.
		self.m_scintilla211 = wx.Window( self.m_panel1011 )
		bSizer411.Add( self.m_scintilla211, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel1011.SetSizer( bSizer411 )
		self.m_panel1011.Layout()
		bSizer411.Fit( self.m_panel1011 )
		self.m_panel1211 = wx.Panel( self.m_splitter311, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer711 = wx.BoxSizer( wx.VERTICAL )


		self.m_panel1211.SetSizer( bSizer711 )
		self.m_panel1211.Layout()
		bSizer711.Fit( self.m_panel1211 )
		self.m_splitter311.SplitHorizontally( self.m_panel1011, self.m_panel1211, 300 )
		bSizer211.Add( self.m_splitter311, 1, wx.EXPAND, 3 )


		bSizer22.Add( bSizer211, 1, wx.EXPAND, 5 )


		self.m_panel26.SetSizer( bSizer22 )
		self.m_panel26.Layout()
		bSizer22.Fit( self.m_panel26 )
		self.m_notebook4.AddPage( self.m_panel26, u"a page", False )

		gSizer2.Add( self.m_notebook4, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel1.SetSizer( gSizer2 )
		self.m_panel1.Layout()
		gSizer2.Fit( self.m_panel1 )
		self.m_splitter2.SplitVertically( self.m_panel5, self.m_panel1, 236 )
		gSizer1.Add( self.m_splitter2, 1, wx.EXPAND, 3 )


		self.SetSizer( gSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass

	def m_splitter2OnIdle( self, event ):
		self.m_splitter2.SetSashPosition( 236 )
		self.m_splitter2.Unbind( wx.EVT_IDLE )

	def m_splitter3OnIdle( self, event ):
		self.m_splitter3.SetSashPosition( 300 )
		self.m_splitter3.Unbind( wx.EVT_IDLE )

	def m_splitter31OnIdle( self, event ):
		self.m_splitter31.SetSashPosition( 300 )
		self.m_splitter31.Unbind( wx.EVT_IDLE )

	def m_splitter311OnIdle( self, event ):
		self.m_splitter311.SetSashPosition( 300 )
		self.m_splitter311.Unbind( wx.EVT_IDLE )


