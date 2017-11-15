# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov 15 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 853,620 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.scope = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 640,640 ), wx.TAB_TRAVERSAL )
		bSizer2.Add( self.scope, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Signal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer21.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		signal_listChoices = []
		self.signal_list = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, signal_listChoices, 0 )
		self.signal_list.SetSelection( 0 )
		bSizer21.Add( self.signal_list, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Time div", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer4.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		time_div_valChoices = [ u"1", u"2", u"5", u"10", u"20", u"50", u"100", u"200", u"500" ]
		self.time_div_val = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, time_div_valChoices, 0 )
		self.time_div_val.SetSelection( 3 )
		bSizer4.Add( self.time_div_val, 0, wx.ALL, 5 )
		
		time_div_unitChoices = [ u"ns", u"us", u"ms", u"s" ]
		self.time_div_unit = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, time_div_unitChoices, 0 )
		self.time_div_unit.SetSelection( 2 )
		bSizer4.Add( self.time_div_unit, 0, wx.ALL, 5 )
		
		
		bSizer21.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Setup" ), wx.VERTICAL )
		
		self.setup_enable = wx.CheckBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Enable", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.setup_enable, 0, wx.ALL, 5 )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText21 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Vertical", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer41.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		setup_mul_opChoices = [ u"mul", u"div" ]
		self.setup_mul_op = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, setup_mul_opChoices, 0 )
		self.setup_mul_op.SetSelection( 1 )
		bSizer41.Add( self.setup_mul_op, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		setup_mul_valChoices = [ u"1", u"2", u"5", u"10", u"20", u"50", u"100", u"200", u"500", u"1000", u"2000", u"5000" ]
		self.setup_mul_val = wx.Choice( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, setup_mul_valChoices, 0 )
		self.setup_mul_val.SetSelection( 3 )
		bSizer41.Add( self.setup_mul_val, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer1.Add( bSizer41, 0, wx.EXPAND, 5 )
		
		
		bSizer21.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

