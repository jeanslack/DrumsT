#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx
import wx.grid as  gridlib

class PanelOne(wx.Panel):
    """Record lesson panel"""
    def __init__(self, parent):
        """
        """
        self.currdate = None
        wx.Panel.__init__(self, parent=parent, style=wx.TAB_TRAVERSAL)
        
        self.parent = parent
        
        self.InitUI()

    def InitUI(self):
        """"""
        self.datepk = wx.DatePickerCtrl(self, wx.ID_ANY, style=wx.DP_DEFAULT)
        boxDate = wx.StaticBox(self, wx.ID_ANY, ("Setting Date lesson"))
        self.checkStudent = wx.CheckBox(self, wx.ID_ANY, ("Check on whether the student is absent"))
        self.checkTeacher = wx.CheckBox(self, wx.ID_ANY, ("Check on whether the teacher is absent"))
        boxAttendances = wx.StaticBox(self, wx.ID_ANY, ("Attendances Register"))
        notebook = wx.Notebook(self, wx.ID_ANY)
        
        bookOne = wx.Panel(notebook, wx.ID_ANY)
        lab1 = wx.StaticText(bookOne, wx.ID_ANY, ("Chart Reading"))
        lab2 = wx.StaticText(bookOne, wx.ID_ANY, ("Hands/Foots Setting"))
        lab3 = wx.StaticText(bookOne, wx.ID_ANY, ("Rudiments"))
        self.txt1 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        self.txt2 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        self.txt3 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        lab4 = wx.StaticText(bookOne, wx.ID_ANY, ("Independance/Coordination"))
        lab5 = wx.StaticText(bookOne, wx.ID_ANY, ("Elements of Style Rhythm"))
        lab6 = wx.StaticText(bookOne, wx.ID_ANY, ("Linear Phrasing"))
        self.txt4 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        self.txt5 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        self.txt6 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        lab7 = wx.StaticText(bookOne, wx.ID_ANY, ("Others 1"))
        lab8 = wx.StaticText(bookOne, wx.ID_ANY, ("Others 2"))
        lab9 = wx.StaticText(bookOne, wx.ID_ANY, ("Others 3"))
        self.txt7 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        self.txt8 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        self.txt9 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)

        bookTwo = wx.Panel(notebook, wx.ID_ANY)
        bookThree = wx.Panel(notebook, wx.ID_ANY)
        btnExit = wx.Button(self, wx.ID_CANCEL, (""))
        btnOk = wx.Button(self, wx.ID_OK, (""))

        # properties
        self.datepk.SetMinSize((120, 30))
        
        lab1.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab2.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab3.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txt1.SetMinSize((250, 80))
        #self.txt1.SetBackgroundColour('#fffcbf')
        self.txt2.SetMinSize((250, 80))
        self.txt2.SetBackgroundColour('#ffafaa')
        self.txt3.SetMinSize((250, 80))
        self.txt3.SetBackgroundColour('#decfff')
        lab4.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab5.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab6.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txt4.SetMinSize((250, 80))
        self.txt4.SetBackgroundColour('#d9ffdb')
        self.txt5.SetMinSize((250, 80))
        self.txt5.SetBackgroundColour('#aff0ff')
        self.txt6.SetMinSize((250, 80))
        self.txt6.SetBackgroundColour('#ffca64')
        lab7.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab8.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab9.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txt7.SetMinSize((250, 80))
        self.txt7.SetBackgroundColour('#f1ff54')
        self.txt8.SetMinSize((250, 80))
        self.txt8.SetBackgroundColour('#9ab0ff')
        self.txt9.SetMinSize((250, 80))
        self.txt9.SetBackgroundColour('#f79fff')
        # layout
        sizBase = wx.FlexGridSizer(3, 1, 0, 0)
        sizBottom = wx.GridSizer(1, 2, 0, 0)
        sizTables = wx.FlexGridSizer(1, 1, 0, 0)
        sizTop = wx.GridSizer(1, 2, 0, 100)
        sizBookOne = wx.FlexGridSizer(6, 3, 0, 0)
        #boxAttendances.Lower()
        boxPresence = wx.StaticBoxSizer(boxAttendances, wx.VERTICAL)
        sizPresence = wx.FlexGridSizer(2, 1, 0, 0)
        #boxDate.Lower()
        boxDate = wx.StaticBoxSizer(boxDate, wx.VERTICAL)
        boxDate.Add(self.datepk, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizTop.Add(boxDate, 1, wx.ALL | wx.EXPAND, 5)
        sizPresence.Add(self.checkStudent, 0, wx.ALIGN_CENTER | wx.LEFT, 5)
        sizPresence.Add(self.checkTeacher, 0, wx.ALIGN_CENTER | wx.LEFT, 5)
        boxPresence.Add(sizPresence, 1, 0, 0)
        sizTop.Add(boxPresence, 1, wx.ALL | wx.EXPAND, 5)
        sizBase.Add(sizTop, 1, 0, 0)

        sizBookOne.Add(lab1, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(lab2, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(lab3, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt1, 0, wx.ALIGN_CENTER|wx.LEFT, 5)
        sizBookOne.Add(self.txt2, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt3, 0, wx.ALIGN_CENTER|wx.RIGHT, 5)
        sizBookOne.Add(lab4, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(lab5, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(lab6, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt4, 0, wx.ALIGN_CENTER|wx.LEFT, 5)
        sizBookOne.Add(self.txt5, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt6, 0, wx.ALIGN_CENTER|wx.RIGHT, 5)
        sizBookOne.Add(lab7, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(lab8, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(lab9, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt7, 0, wx.ALIGN_CENTER|wx.LEFT, 5)
        sizBookOne.Add(self.txt8, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt9, 0, wx.ALIGN_CENTER|wx.RIGHT, 5)
        bookOne.SetSizer(sizBookOne)
        sizBookOne.AddGrowableRow(0)
        sizBookOne.AddGrowableRow(1)
        sizBookOne.AddGrowableRow(2)
        sizBookOne.AddGrowableRow(3)
        sizBookOne.AddGrowableRow(4)
        sizBookOne.AddGrowableRow(5)
        sizBookOne.AddGrowableCol(1)
        notebook.AddPage(bookOne, ("tab 1"))
        notebook.AddPage(bookTwo, ("tab 2"))
        notebook.AddPage(bookThree, ("tab 3"))
        sizTables.Add(notebook, 1, wx.ALL | wx.EXPAND, 5)
        sizTables.AddGrowableRow(0)
        sizTables.AddGrowableCol(0)
        sizBase.Add(sizTables, 1, wx.EXPAND, 0)
        sizBottom.Add(btnExit, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        sizBottom.Add(btnOk, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        sizBase.Add(sizBottom, 1, wx.EXPAND, 0)#####
        self.SetSizer(sizBase)
        sizBase.Fit(self)
        sizBase.AddGrowableRow(1)
        sizBase.AddGrowableCol(0)
        
        self.currdate = self.datepk.GetValue()
        
        ## BINDING
        self.Bind(wx.EVT_DATE_CHANGED, self.onDate, self.datepk)
        #self.Bind(wx.EVT_CLOSE, self.on_close)
        #self.Bind(wx.EVT_BUTTON, self.on_close, btnExit)
        btnExit.Bind(wx.EVT_BUTTON, self.on_close)
        
    #-----------------------HANDLING----------------------------------------------#
    def on_close(self, event):
        #self.parent.Show()
        self.parent.Destroy()
        event.Skip()
        #-------------------------------------------------------------------#
    def onDate(self, event):
        self.currdate = self.datepk.GetValue()
###############################################################################
class MyForm(wx.Panel):
 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, style=wx.TAB_TRAVERSAL)
 
        # Add a panel so it looks the correct on all platforms
        #panel = wx.Panel(self, wx.ID_ANY)
        self.grid = gridlib.Grid(self)
        self.grid.CreateGrid(200,8)
        self.grid.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK,
                       self.showPopupMenu)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND, 5)
        self.SetSizer(sizer)
        sizer.Fit(self)
 
    #----------------------------------------------------------------------
    def showPopupMenu(self, event):
        """
        Create and display a popup menu on right-click event
        """
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popupID2 = wx.NewId()
            self.popupID3 = wx.NewId()
            # make a menu
 
        menu = wx.Menu()
        # Show how to put an icon in the menu
        item = wx.MenuItem(menu, self.popupID1,"One")
        menu.AppendItem(item)
        menu.Append(self.popupID2, "Two")
        menu.Append(self.popupID3, "Three")
 
        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()
        
###############################################################################
class Lesson(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------#
    def __init__(self):
        """Constructor"""
        
        self.drumsT_ico = wx.GetApp().drumsT_icon
        self.tab_ico = wx.GetApp().tab_icon
        self.lesson_ico = wx.GetApp().lesson_icon
        
        wx.Frame.__init__(self, None, title='Test')
        self.tool_bar()
        
        self.panel_one = PanelOne(self)
        self.panel_two = MyForm(self)
        self.panel_two.Hide()
        
        self.sizer = wx.FlexGridSizer(1, 1, 0, 0)
        self.sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.sizer.AddGrowableRow(0)
        self.sizer.AddGrowableCol(0)
        
        
        
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap(self.drumsT_ico, wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        
        self.SetMinSize((795, 530))
        self.CentreOnScreen()
        self.SetSizer(self.sizer)
        self.Layout()
        
        self.toolbar.EnableTool(wx.ID_FILE2, False)
        
        self.Bind(wx.EVT_CLOSE, self.on_close)
        
    #-----------------------HANDLING----------------------------------------#
    def on_close(self, event):
        #self.parent.Show()
        self.Destroy()
        #event.Skip()
    #-------------------------------------------------------------------#
        
    ######################################################################
    #------------------------Build the Tool Bar--------------------------#
    ######################################################################
    def tool_bar(self):
        """
        Makes and attaches the view tools bar
        """
        #--------- Properties
        self.toolbar = self.CreateToolBar(style=(wx.TB_HORZ_LAYOUT | wx.TB_TEXT))
        self.toolbar.SetToolBitmapSize((16,16))
        self.toolbar.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        
        # ------- See student data
        pantab = self.toolbar.AddLabelTool(wx.ID_FILE2, 'Rec lesson',
                                          wx.Bitmap(self.lesson_ico))
        self.toolbar.AddSeparator()
        
        # ------- Add new student
        panlesson = self.toolbar.AddLabelTool(wx.ID_FILE3, 'Open Tables', 
                                             wx.Bitmap(self.tab_ico))
        self.toolbar.AddSeparator()
        
        # ----------- finally, create it
        self.toolbar.Realize()
        
        #------------ Binding
        self.Bind(wx.EVT_TOOL, self.panTab, pantab)
        self.Bind(wx.EVT_TOOL, self.panLesson, panlesson)
        
    #-------------------------EVENTS-----------------------------------#
    #------------------------------------------------------------------#
    def panTab(self, event):
        if self.panel_two.IsShown():
            self.SetTitle("Panel One Showing")
            self.panel_one.Show()
            self.panel_two.Hide()
            self.toolbar.EnableTool(wx.ID_FILE3, True)
            self.toolbar.EnableTool(wx.ID_FILE2, False)
            self.Layout()
    #------------------------------------------------------------------#
    def panLesson(self, event):
        """
        Add one new record to Class table
        """
        if self.panel_one.IsShown():
            self.SetTitle("Panel Two Showing")
            self.panel_one.Hide()
            self.panel_two.Show()
            self.toolbar.EnableTool(wx.ID_FILE3, False)
            self.toolbar.EnableTool(wx.ID_FILE2, True)
            self.Layout()
        #self.Show()
 
#if __name__ == '__main__':
    #app = wx.App(False)
    #frame = MyFrame()
    #app.MainLoop()
