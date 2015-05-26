#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import wx



class PanelOne(wx.Panel):
    
    def __init__(self, parent):

        wx.Panel.__init__(self, parent, style=wx.BORDER_SUNKEN | wx.TAB_TRAVERSAL)

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
        self.txt1 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.txt2 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.txt3 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        lab4 = wx.StaticText(bookOne, wx.ID_ANY, ("Independance/Coordination"))
        lab5 = wx.StaticText(bookOne, wx.ID_ANY, ("Elements of Style Rhythm"))
        lab6 = wx.StaticText(bookOne, wx.ID_ANY, ("Linear Phrasing"))
        self.txt4 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.txt5 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.txt6 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        lab7 = wx.StaticText(bookOne, wx.ID_ANY, ("Others 1"))
        lab8 = wx.StaticText(bookOne, wx.ID_ANY, ("Others 2"))
        lab9 = wx.StaticText(bookOne, wx.ID_ANY, ("Others 3"))
        self.txt7 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.txt8 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE)
        self.txt9 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE)

        bookTwo = wx.Panel(notebook, wx.ID_ANY)
        bookThree = wx.Panel(notebook, wx.ID_ANY)
        btnExit = wx.Button(self, wx.ID_ANY, ("button_2"))
        btnOk = wx.Button(self, wx.ID_ANY, ("button_3"))

        # properties
        self.datepk.SetMinSize((120, 30))
        
        lab1.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab2.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab3.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txt1.SetMinSize((300, 130))
        #self.txt1.SetBackgroundColour('#fffcbf')
        self.txt2.SetMinSize((300, 130))
        self.txt2.SetBackgroundColour('#ffafaa')
        self.txt3.SetMinSize((300, 130))
        self.txt3.SetBackgroundColour('#decfff')
        lab4.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab5.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab6.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txt4.SetMinSize((300, 130))
        self.txt4.SetBackgroundColour('#d9ffdb')
        self.txt5.SetMinSize((300, 130))
        self.txt5.SetBackgroundColour('#aff0ff')
        self.txt6.SetMinSize((300, 130))
        self.txt6.SetBackgroundColour('#ffca64')
        lab7.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab8.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        lab9.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txt7.SetMinSize((300, 130))
        self.txt7.SetBackgroundColour('#f1ff54')
        self.txt8.SetMinSize((300, 130))
        self.txt8.SetBackgroundColour('#9ab0ff')
        self.txt9.SetMinSize((300, 130))
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
        sizBookOne.Add(self.txt1, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt2, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt3, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(lab4, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(lab5, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(lab6, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt4, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt5, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt6, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(lab7, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(lab8, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(lab9, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt7, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt8, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt9, 0, wx.ALIGN_CENTER, 0)
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
        sizBottom.Add(btnExit, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizBottom.Add(btnOk, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
        sizBase.Add(sizBottom, 1, 0, 0)
        self.SetSizer(sizBase)
        sizBase.Fit(self)
        sizBase.AddGrowableRow(1)
        sizBase.AddGrowableCol(0)

class Lesson(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        #self.drumsT_ico = wx.GetApp().drumsT_icon
        
        wx.Frame.__init__(self, None, title='Test')
        panel = PanelOne(self)
        
        #icon = wx.EmptyIcon()
        #icon.CopyFromBitmap(wx.Bitmap(self.drumsT_ico, wx.BITMAP_TYPE_ANY))
        #self.SetIcon(icon)
        
        self.SetMinSize((1000, 730))
        self.CentreOnScreen()
        self.Layout()
        
        
        #self.Show()
 
#if __name__ == '__main__':
    #app = wx.App(False)
    #frame = MyFrame()
    #app.MainLoop()
