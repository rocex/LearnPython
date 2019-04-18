"""Subclass of DataStudioUI, which is generated by wxFormBuilder."""

import wx
import DataStudioUI

# Implementing DataStudioUI
class DataStudio( DataStudioUI.DataStudioUI ):
	def __init__( self, parent ):
		DataStudioUI.DataStudioUI.__init__( self, parent )

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = DataStudio(None)
    frm.Show()
    app.MainLoop()