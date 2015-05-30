#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: add_lesson.py
# Porpose: Add a new lesson recording
# Author: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (00) 28/05/2015
#########################################################

import wx
from drumsT_SYS.SQLite_lib import School_Class

class PanelOne(wx.Panel):
    """
    Record lesson panel 
    """
    def __init__(self, parent, nameSur, IDclass, path_db):
        """
        Shows the interface for data entry on the current lesson.
        """
        wx.Panel.__init__(self, parent, -1, style=wx.TAB_TRAVERSAL)
        self.currdate = None # current date
        self.switch = False # switch for check absences
        self.nameSur = nameSur # name/surname of student
        self.IDclass = IDclass # Id of Class table
        self.path_db = path_db # database filename
        self.parent = parent 
        
        self.InitUI()

    def InitUI(self):
        """
        Start with widget and panel setup
        """
        self.datepk = wx.DatePickerCtrl(self, wx.ID_ANY, style=wx.DP_DEFAULT)
        boxDate = wx.StaticBox(self, wx.ID_ANY, ("Setting Date lesson"))
        self.rdb = wx.RadioBox(self, wx.ID_ANY, ("Attendances Register"), 
                               choices=[("All Present"),
                                        ("Student is absent"),
                                        ("Teacher is absent"),
                                        ],
                               majorDimension=0,style=wx.RA_SPECIFY_COLS
                               )
        notebook = wx.Notebook(self, wx.ID_ANY)
        #### insert widget in first notebook table
        bookOne = wx.Panel(notebook, wx.ID_ANY)
        self.lab1 = wx.StaticText(bookOne, wx.ID_ANY, ("Chart Reading"))
        self.lab2 = wx.StaticText(bookOne, wx.ID_ANY, ("Hands/Foots Setting"))
        self.lab3 = wx.StaticText(bookOne, wx.ID_ANY, ("Rudiments"))
        self.txt1 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        self.txt2 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        self.txt3 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        self.lab4 = wx.StaticText(bookOne, wx.ID_ANY, ("Independance/Coordination"))
        self.lab5 = wx.StaticText(bookOne, wx.ID_ANY, ("Elements of Style Rhythm"))
        self.lab6 = wx.StaticText(bookOne, wx.ID_ANY, ("Minus One"))
        self.txt4 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        self.txt5 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        self.txt6 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        self.lab7 = wx.StaticText(bookOne, wx.ID_ANY, ("Others 1"))
        self.lab8 = wx.StaticText(bookOne, wx.ID_ANY, ("Others 2"))
        self.lab9 = wx.StaticText(bookOne, wx.ID_ANY, ("Others 3"))
        self.txt7 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        self.txt8 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        self.txt9 = wx.TextCtrl(bookOne, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                wx.TE_PROCESS_ENTER)
        #### insert widget in second notebook table
        bookTwo = wx.Panel(notebook, wx.ID_ANY)
        self.lab10 = wx.StaticText(bookTwo, wx.ID_ANY, ("Votes/Report"))
        self.txt10 = wx.TextCtrl(bookTwo, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                 wx.TE_PROCESS_ENTER)
        self.lab11 = wx.StaticText(bookTwo, wx.ID_ANY, ("Reminder/Block-notes"))
        self.txt11 = wx.TextCtrl(bookTwo, wx.ID_ANY, "", style=wx.TE_MULTILINE|
                                 wx.TE_PROCESS_ENTER)
        #### notebook 3
        #bookThree = wx.Panel(notebook, wx.ID_ANY) #NOTE for third notebook table
        btnExit = wx.Button(self, wx.ID_EXIT, (""))
        self.btnOk = wx.Button(self, wx.ID_OK, (""))

        #---------------------------------------------- PROPERTIES
        self.datepk.SetMinSize((150, 24))
        self.lab1.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.lab2.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.lab3.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txt1.SetMinSize((250, 80))
        self.txt2.SetMinSize((250, 80))
        self.txt3.SetMinSize((250, 80))
        self.lab4.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.lab5.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.lab6.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txt4.SetMinSize((250, 80))
        self.txt5.SetMinSize((250, 80))
        self.txt6.SetMinSize((250, 80))
        self.lab7.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.lab8.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.lab9.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txt7.SetMinSize((250, 80))
        self.txt8.SetMinSize((250, 80))
        self.txt9.SetMinSize((250, 80))
        self.lab10.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.lab11.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.txt11.SetBackgroundColour('#fff96f')#yellow
        #-------------------------------------------------- LAYOUT
        sizBase = wx.FlexGridSizer(3, 1, 0, 0)
        sizBottom = wx.GridSizer(1, 2, 0, 0)
        sizTables = wx.FlexGridSizer(1, 1, 0, 0)
        sizTop = wx.FlexGridSizer(1, 2, 0, 20)
        sizBookOne = wx.FlexGridSizer(6, 3, 0, 0)
        sizBookTwo = wx.FlexGridSizer(2, 2, 0, 0)
        #boxDate.Lower()
        boxDate = wx.StaticBoxSizer(boxDate, wx.VERTICAL)
        boxDate.Add(self.datepk, 0, wx.ALIGN_CENTER | wx.ALL, 0)
        sizTop.Add(boxDate, 1, wx.EXPAND|wx.ALL, 5)
        sizTop.Add(self.rdb, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        sizBase.Add(sizTop, 1, 0, 0)
        #### Set first table of notebook
        sizBookOne.Add(self.lab1, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.lab2, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.lab3, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt1, 0, wx.ALIGN_CENTER|wx.LEFT, 5)
        sizBookOne.Add(self.txt2, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt3, 0, wx.ALIGN_CENTER|wx.RIGHT, 5)
        sizBookOne.Add(self.lab4, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.lab5, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.lab6, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt4, 0, wx.ALIGN_CENTER|wx.LEFT, 5)
        sizBookOne.Add(self.txt5, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.txt6, 0, wx.ALIGN_CENTER|wx.RIGHT, 5)
        sizBookOne.Add(self.lab7, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.lab8, 0, wx.ALIGN_CENTER, 0)
        sizBookOne.Add(self.lab9, 0, wx.ALIGN_CENTER, 0)
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
        sizBookTwo.Add(self.lab10, 0, wx.ALL, 5)
        sizBookTwo.Add(self.lab11, 0, wx.ALL, 5)
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
        sizBottom.Add(btnExit, 0, wx.ALIGN_LEFT | wx.ALL, 15)
        sizBottom.Add(self.btnOk, 0, wx.ALIGN_RIGHT | wx.ALL, 15)
        sizBase.Add(sizBottom, 1, wx.EXPAND, 0)#####
        self.SetSizer(sizBase)
        sizBase.Fit(self)
        sizBase.AddGrowableRow(1)
        sizBase.AddGrowableCol(0)
        
        self.currdate = self.datepk.GetValue() 
        
        ######################## binding #####################
        self.Bind(wx.EVT_DATE_CHANGED, self.onDate, self.datepk)
        self.Bind(wx.EVT_RADIOBOX, self.onAbsences, self.rdb)
        btnExit.Bind(wx.EVT_BUTTON, self.on_close)
        self.Bind(wx.EVT_BUTTON, self.onOk, self.btnOk)
        
    ######################## Events Handler
    #-----------------------------------------------------------------------#
    def on_close(self, event):
        self.parent.Destroy()
        #event.Skip()
    #-----------------------------------------------------------------------#
    def onDate(self, event):
        self.currdate = self.datepk.GetValue()
    #-----------------------------------------------------------------------#
    def onAbsences(self, event):
        """
        Enable or disable widget in sizBookOne only, when radiobox 
        is check. To prevent repetitive processes for Enable() and 
        Disable() methods i have not been able (or I did not want) 
        to find better solution that self.switch
        """
        if self.rdb.GetSelection() == 0:
            if self.switch:
                self.switch = False
                self.txt1.Enable(), self.txt2.Enable(), self.txt3.Enable()
                self.txt4.Enable(), self.txt5.Enable(), self.txt6.Enable() 
                self.txt7.Enable(), self.txt8.Enable(), self.txt9.Enable()
                self.lab1.Enable(), self.lab2.Enable(), self.lab3.Enable()
                self.lab4.Enable(), self.lab5.Enable(), self.lab6.Enable() 
                self.lab7.Enable(), self.lab8.Enable(), self.lab9.Enable()

        elif self.rdb.GetSelection() == 1 or self.rdb.GetSelection() == 2:
            if not self.switch:
                self.switch = True
                self.txt1.SetValue(''), self.txt2.SetValue('')
                self.txt3.SetValue(''), self.txt4.SetValue('')
                self.txt5.SetValue(''), self.txt6.SetValue('')
                self.txt7.SetValue(''), self.txt8.SetValue('')
                self.txt9.SetValue('')
                self.txt1.Disable(), self.txt2.Disable(), self.txt3.Disable()
                self.txt4.Disable(), self.txt5.Disable(), self.txt6.Disable() 
                self.txt7.Disable(), self.txt8.Disable(), self.txt9.Disable()
                
                self.lab1.Disable(), self.lab2.Disable(), self.lab3.Disable()
                self.lab4.Disable(), self.lab5.Disable(), self.lab6.Disable() 
                self.lab7.Disable(), self.lab8.Disable(), self.lab9.Disable()
    #-----------------------------------------------------------------------#
    def onOk(self, event):
        """
        
        """
        msg = ("Are you sure to record this lesson ?")
        warn = wx.MessageDialog(self, msg, "Question", wx.YES_NO | 
                                    wx.CANCEL | wx.ICON_QUESTION)
            
        if warn.ShowModal() == wx.ID_YES:
            pass
        else:
            return
        
        absences = u"%s" % (self.rdb.GetItemLabel(self.rdb.GetSelection()))
        date = u"%s" % (self.currdate)
        arg1 = u"""%s""" % (self.txt1.GetValue().strip())
        arg2 = u"""%s""" % (self.txt2.GetValue().strip())
        arg3 = u"""%s""" % (self.txt3.GetValue().strip())
        arg4 = u"""%s""" % (self.txt4.GetValue().strip())
        arg5 = u"""%s""" % (self.txt5.GetValue().strip())
        arg6 = u"""%s""" % (self.txt6.GetValue().strip())
        arg7 = u"""%s""" % (self.txt7.GetValue().strip())
        arg8 = u"""%s""" % (self.txt8.GetValue().strip())
        arg9 = u"""%s""" % (self.txt9.GetValue().strip())
        arg10 = u"""%s""" % ( self.txt10.GetValue().strip())
        arg11 = u"""%s""" % ( self.txt11.GetValue().strip())

        listObj = [self.IDclass, absences, date, arg1, arg2, arg3, arg4, 
                   arg5, arg6, arg7, arg8, arg9, arg10, arg11, 
                   ]
        for n, item in enumerate(listObj):# if empty str fill out with NONE str
            if item == '':
                listObj[n] = 'NONE'

        lesson = School_Class().lessons(listObj, self.path_db)
        
        if lesson[0]:
            wx.MessageBox(lesson[1], 'ERROR', wx.ICON_ERROR, self)
            self.btnOk.Disable()
            return
        
        wx.MessageBox("Successfull storing !", "Info", wx.OK, self)
        
        self.btnOk.Disable()
