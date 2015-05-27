#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx
import wx.grid as  gridlib

class PanelOne(wx.Panel):
    """Record lesson panel"""
    def __init__(self, parent):
        """
        Shows the interface for data entry on the current lesson
        """
        wx.Panel.__init__(self, parent, -1, style=wx.TAB_TRAVERSAL)
        self.currdate = None
        self.parent = parent
        
        self.InitUI()

    def InitUI(self):
        """"""
        self.datepk = wx.DatePickerCtrl(self, wx.ID_ANY, style=wx.DP_DEFAULT)
        boxDate = wx.StaticBox(self, wx.ID_ANY, ("Setting Date lesson"))
        self.checkStudent = wx.CheckBox(self, wx.ID_ANY, (
                                     "Check on whether the student is absent"))
        self.checkTeacher = wx.CheckBox(self, wx.ID_ANY, (
                                     "Check on whether the teacher is absent"))
        boxAttendances = wx.StaticBox(self, wx.ID_ANY, ("Attendances Register"))
        notebook = wx.Notebook(self, wx.ID_ANY)
        #### insert widget in first notebook table
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
        #### insert widget in second notebook table
        bookTwo = wx.Panel(notebook, wx.ID_ANY)
        lab10 = wx.StaticText(bookTwo, wx.ID_ANY, ("Votes/Report"))
        self.txt10 = wx.TextCtrl(bookTwo, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                 wx.TE_PROCESS_ENTER)
        lab11 = wx.StaticText(bookTwo, wx.ID_ANY, ("Reminder/Block-notes"))
        self.txt11 = wx.TextCtrl(bookTwo, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                 wx.TE_PROCESS_ENTER)
        #### notebook 3
        #bookThree = wx.Panel(notebook, wx.ID_ANY) #NOTE for third notebook table
        btnExit = wx.Button(self, wx.ID_CANCEL, (""))
        btnOk = wx.Button(self, wx.ID_OK, (""))

        #---------------------------------------------- PROPERTIES
        self.datepk.SetMinSize((120, 30))
        lab1.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab2.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab3.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txt1.SetMinSize((250, 80))
        self.txt2.SetMinSize((250, 80))
        self.txt3.SetMinSize((250, 80))
        lab4.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab5.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab6.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txt4.SetMinSize((250, 80))
        self.txt5.SetMinSize((250, 80))
        self.txt6.SetMinSize((250, 80))
        lab7.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab8.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab9.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txt7.SetMinSize((250, 80))
        self.txt8.SetMinSize((250, 80))
        self.txt9.SetMinSize((250, 80))
        lab10.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab11.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txt11.SetBackgroundColour('#fff96f')
        #-------------------------------------------------- LAYOUT
        sizBase = wx.FlexGridSizer(3, 1, 0, 0)
        sizBottom = wx.GridSizer(1, 2, 0, 0)
        sizTables = wx.FlexGridSizer(1, 1, 0, 0)
        sizTop = wx.GridSizer(1, 2, 0, 100)
        sizBookOne = wx.FlexGridSizer(6, 3, 0, 0)
        sizBookTwo = wx.FlexGridSizer(2, 2, 0, 0)
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
        #### Set first table of notebook
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
        #### Set second table of notebook
        sizBookTwo.Add(lab10, 0, wx.ALL, 5)
        sizBookTwo.Add(lab11, 0, wx.ALL, 5)
        sizBookTwo.Add(self.txt10, 0, wx.EXPAND|wx.ALIGN_CENTER|wx.ALL, 5)
        sizBookTwo.Add(self.txt11, 0, wx.EXPAND|wx.ALIGN_CENTER|wx.ALL, 5)
        bookTwo.SetSizer(sizBookTwo)
        #sizBookTwo.AddGrowableRow(0)
        sizBookTwo.AddGrowableRow(1)
        sizBookTwo.AddGrowableCol(0)
        sizBookTwo.AddGrowableCol(1)
        notebook.AddPage(bookOne, ("Study Arguments"))
        notebook.AddPage(bookTwo, ("Vote and Reminder"))
        #notebook.AddPage(bookThree, ("tab 3")) #NOTE for third notebook table
        sizTables.Add(notebook, 1, wx.ALL | wx.EXPAND, 5)
        sizTables.AddGrowableRow(0)
        sizTables.AddGrowableCol(0)
        #### 
        sizBase.Add(sizTables, 1, wx.EXPAND, 0)
        sizBottom.Add(btnExit, 0, wx.ALIGN_LEFT | wx.ALL, 5)
        sizBottom.Add(btnOk, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        sizBase.Add(sizBottom, 1, wx.EXPAND, 0)#####
        self.SetSizer(sizBase)
        sizBase.Fit(self)
        sizBase.AddGrowableRow(1)
        sizBase.AddGrowableCol(0)
        
        self.currdate = self.datepk.GetValue()
        
        
        #------------------------------------------------------- BINDING
        self.Bind(wx.EVT_DATE_CHANGED, self.onDate, self.datepk)
        self.Bind(wx.EVT_CHECKBOX, self.absentStudent, self.checkStudent)
        btnExit.Bind(wx.EVT_BUTTON, self.on_close)
        self.Bind(wx.EVT_BUTTON, self.onOk, btnOk)
        
    #-----------------------HANDLING----------------------------------------#
    def on_close(self, event):
        self.parent.Destroy()
        #event.Skip()
    #-----------------------------------------------------------------------#
    def onDate(self, event):
        self.currdate = self.datepk.GetValue()
    #-----------------------------------------------------------------------#
    def absentStudent(self, event):
        
        if self.checkStudent.IsChecked() and self.checkTeacher.IsChecked():
            pass
        else:
            #self.txt1.SetValue(''), self.txt2.SetValue('')
            #self.txt3.SetValue(''), self.txt4.SetValue('')
            #self.txt5.SetValue(''), self.txt6.SetValue('')
            #self.txt7.SetValue(''), self.txt8.SetValue('')
            #self.txt9.SetValue('')
            #self.txt1.Hide(), self.txt2.Hide(), self.txt3.Hide()
            #self.txt4.Hide(), self.txt5.Hide(), self.txt6.Hide() 
            #self.txt7.Hide(), self.txt8.Hide(), self.txt9.Hide()
            
    def absentTeacher(self, event):
        
        if self.checkTeacher.IsChecked() and self.checkStudent.IsChecked():
            pass
        else:
            #self.txt1.SetValue(''), self.txt2.SetValue('')
            #self.txt3.SetValue(''), self.txt4.SetValue('')
            #self.txt5.SetValue(''), self.txt6.SetValue('')
            #self.txt7.SetValue(''), self.txt8.SetValue('')
            #self.txt9.SetValue('')
            #self.txt1.Hide(), self.txt2.Hide(), self.txt3.Hide()
            #self.txt4.Hide(), self.txt5.Hide(), self.txt6.Hide() 
            #self.txt7.Hide(), self.txt8.Hide(), self.txt9.Hide()
            
        
            
            
        
    #-----------------------------------------------------------------------#
    def onOk(self, event):
        
        arg1 = self.txt1.GetValue()
        arg2 = self.txt2.GetValue()
        arg3 = self.txt3.GetValue()
        arg4 = self.txt4.GetValue()
        arg5 = self.txt5.GetValue()
        arg6 = self.txt6.GetValue()
        arg7 = self.txt7.GetValue()
        arg8 = self.txt8.GetValue()
        arg9 = self.txt9.GetValue()
        arg10 = self.txt10.GetValue()
        arg11 = self.txt11.GetValue()
        date = self.currdate
        if self.checkStudent.GetValue():
            absentS = 'absent'
        else:
            absentS = 'present'
            
        if self.checkTeacher.GetValue():
            absentT = 'absent'
        else:
            absentT = 'present'
        
        print arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, date, absentS, absentT
        
        
        
###############################################################################
class MyForm(wx.Panel):
 
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.TAB_TRAVERSAL)
        myGrid = gridlib.Grid(self)
        myGrid.CreateGrid(365, 6)
        
        myGrid.SetCellValue(0,0, "Hello")
        myGrid.SetCellFont(0, 0, wx.Font(12, wx.ROMAN, wx.ITALIC, wx.NORMAL))
        print myGrid.GetCellValue(0,0)
        
        myGrid.SetCellValue(1,1, "I'm in red!")
        myGrid.SetCellTextColour(1, 1, wx.RED)
        
        myGrid.SetCellBackgroundColour(2, 2, wx.CYAN)
        
        myGrid.SetCellValue(3, 3, "This cell is read-only")
        myGrid.SetReadOnly(3, 3, True)
        
        myGrid.SetCellEditor(5, 0, gridlib.GridCellNumberEditor(1,1000))
        myGrid.SetCellValue(5, 0, "123")
        myGrid.SetCellEditor(6, 0, gridlib.GridCellFloatEditor())
        myGrid.SetCellValue(6, 0, "123.34")
        myGrid.SetCellEditor(7, 0, gridlib.GridCellNumberEditor())
        
        myGrid.SetCellSize(11, 1, 3, 3)
        myGrid.SetCellAlignment(11, 1, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        myGrid.SetCellValue(11, 1, "This cell is set to span 3 rows and 3 columns")
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, 1, wx.EXPAND, 5)
        self.SetSizer(sizer)
        sizer.Fit(self)
        
        
        
        #self.grid = gridlib.Grid(self)
        #self.grid.CreateGrid(200,8)
 
        #sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(self.grid, 1, wx.EXPAND, 5)
        #self.SetSizer(sizer)
        #sizer.Fit(self)

        
###############################################################################
class Lesson(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------#
    def __init__(self, namesur):
        """Constructor"""
        
        # set attributes:
        self.drumsT_ico = wx.GetApp().drumsT_icon
        self.tab_ico = wx.GetApp().tab_icon
        self.lesson_ico = wx.GetApp().lesson_icon
        self.nameSur = namesur # name surname on title
        
        wx.Frame.__init__(self, None, -1, style=wx.DEFAULT_FRAME_STYLE)
        self.tool_bar()
        
        self.panel_one = PanelOne(self)
        self.panel_two = MyForm(self)
        self.panel_two.Hide()
        
        self.sizer = wx.FlexGridSizer(1, 1, 0, 0)
        self.sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.sizer.Add(self.panel_two, 1, wx.EXPAND|wx.ALL, 10)
        self.sizer.AddGrowableRow(0)
        self.sizer.AddGrowableCol(0)
        
        
        #################### Properties
        self.SetTitle(("Day Lesson - %s" % self.nameSur))
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap(self.drumsT_ico, wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        
        self.SetMinSize((795, 530))
        self.CentreOnScreen()
        self.SetSizer(self.sizer)
        self.Layout()
        
        #self.Show()# for stand-alone case only
        
        self.toolbar.EnableTool(wx.ID_FILE2, False)
        
        self.Bind(wx.EVT_CLOSE, self.on_close)
        
    #-----------------------HANDLING------------------------------------#
    def on_close(self, event):
        self.Destroy()
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
        pantab = self.toolbar.AddLabelTool(wx.ID_FILE2, "Day lesson",
                                           wx.Bitmap(self.lesson_ico))
        self.toolbar.AddSeparator()
        
        # ------- Add new student
        panlesson = self.toolbar.AddLabelTool(wx.ID_FILE3, "Open Tables" , 
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
            self.SetTitle("Day Lesson - %s" % self.nameSur)
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
            self.SetTitle("Panoramic Table - %s" % self.nameSur)
            self.panel_one.Hide()
            self.panel_two.Show()
            self.toolbar.EnableTool(wx.ID_FILE3, False)
            self.toolbar.EnableTool(wx.ID_FILE2, True)
            self.Layout()
        
 
#if __name__ == '__main__':
    #app = wx.App(False)
    #frame = Lesson()
    #app.MainLoop()
