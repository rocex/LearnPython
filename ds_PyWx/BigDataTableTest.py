import wx
import wx.xrc
import wx.grid
import threading
import time


class BigDataTableTest(wx.Frame):

    cols = 50
    rows = 100000

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            858, 557), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_statusBar3 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.m_menubar3 = wx.MenuBar(0)
        self.m_menu = wx.Menu()
        self.m_menuItem1 = wx.MenuItem(
            self.m_menu, wx.ID_ANY, u"填充", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu.Append(self.m_menuItem1)

        self.m_menuItem2 = wx.MenuItem(
            self.m_menu, wx.ID_ANY, u"清空", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu.Append(self.m_menuItem2)

        self.m_menubar3.Append(self.m_menu, u"File")

        self.SetMenuBar(self.m_menubar3)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_grid2 = wx.grid.Grid(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid2.CreateGrid(0, self.cols)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.EnableDragGridSize(False)
        self.m_grid2.SetMargins(0, 0)

        # Columns
        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelSize(30)
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelSize(80)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer1.Add(self.m_grid2, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        self.Bind(wx.EVT_MENU, self.m_menuItem1MenuSelection,
                  id=self.m_menuItem1.GetId())
        self.Bind(wx.EVT_MENU, self.m_menuItem2MenuSelection,
                  id=self.m_menuItem2.GetId())

    def m_menuItem1MenuSelection(self, event):
        self.cleanData()
        bl = self.m_grid2.AppendRows(self.rows)

        if bl:
            t = threading.Thread(target=frm.fillData)
            t.setDaemon(True)
            t.start()
            # t.join()
            # self.fillData()

    def m_menuItem2MenuSelection(self, event):
        t = threading.Thread(target=frm.cleanData)
        t.setDaemon(True)
        t.start()
        # t.join()

    def __del__(self):
        pass

    def fillData(self):
        # pass
        for row in range(self.rows):
            for col in range(self.cols):
                self.m_grid2.SetCellValue(row, col,
                                          "row: {row},col: {col}".format(row=row + 1, col=col + 1))

    def cleanData(self):
        self.m_grid2.ClearGrid()

        if self.m_grid2.GetNumberRows() > 0:
            self.m_grid2.DeleteRows(0, self.m_grid2.GetNumberRows())


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = BigDataTableTest(None)
    frm.Show()
    app.MainLoop()
