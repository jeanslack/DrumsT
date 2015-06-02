#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: lesson_prospective.py
# Porpose: Show some data lessons of a one student
# Author: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (00) 28/05/2015
#########################################################

import wx
import wx.grid as  gridlib
from drumsT_SYS.SQLite_lib import School_Class

class PanelTwo(wx.Panel):
    """
    Show a grid with tabular data
    """
    def __init__(self, parent, nameSur, IDclass, path_db):
        """
        Display a list with general data of all previous lessons
        of the student in object and relating only to selected 
        the school year
        """
        self.currentlySelectedCell = (0, 0)
        self.rowEdit = None
        self.commNew = []
        self.commLast = []
        self.index = 0
        self.path_db = path_db
        self.IDclass = IDclass
        wx.Panel.__init__(self, parent, -1, style=wx.TAB_TRAVERSAL)
        self.comBtn = wx.Button(self, wx.ID_ANY, ("Commit Change"))
        self.uncomBtn = wx.Button(self, wx.ID_ANY, ("Uncommit Last"))
        self.applyBtn = wx.Button(self, wx.ID_ANY, ("Apply Commit"))
        self.myGrid = gridlib.Grid(self)
        self.myGrid.EnableEditing(False) # make all in read only
        self.myGrid.CreateGrid(150, 15)
        self.myGrid.SetColLabelValue(0, "ID lesson")
        self.myGrid.SetColLabelValue(1, "ID class")
        self.myGrid.SetColLabelValue(2, "Attendances")
        self.myGrid.SetColLabelValue(3, "Lesson Date")
        self.myGrid.SetColLabelValue(4, "Chart Reading")
        self.myGrid.SetColLabelValue(5, "Hands/foots Setting")
        self.myGrid.SetColLabelValue(6, "Rudiments")
        self.myGrid.SetColLabelValue(7, "Coordination")
        self.myGrid.SetColLabelValue(8, "Styles")
        self.myGrid.SetColLabelValue(9, "Minus One")
        self.myGrid.SetColLabelValue(10, "Other-1")
        self.myGrid.SetColLabelValue(11, "Other-2")
        self.myGrid.SetColLabelValue(12, "Other-3")
        self.myGrid.SetColLabelValue(13, "Votes")
        self.myGrid.SetColLabelValue(14, "Note/Reminder")
        #### set columns 0-1-2 in read only
        #attr = gridlib.GridCellAttr()
        #attr.SetReadOnly(True)
        #self.myGrid.SetColAttr(0, attr)
        #self.myGrid.SetColAttr(1, attr)
        #self.myGrid.SetColAttr(2, attr)
        ## oppure: self.myGrid.SetReadOnly(3, 3, True)
        self.setting()
        sizer = wx.BoxSizer(wx.VERTICAL)
        box = wx.GridSizer(1,3,0,40)
        sizer.Add(self.myGrid, 1, wx.EXPAND, 5)
        #sizer.Add(self.comBtn, 0, wx.ALL, 5)
        #sizer.Add(self.uncomBtn, 0, wx.ALL, 5)
        sizer.Add(box, 0, wx.ALL, 5)
        box.Add(self.comBtn, 0, wx.ALL, 5)
        box.Add(self.uncomBtn, 0, wx.ALL, 5)
        box.Add(self.applyBtn, 0, wx.ALL, 5)
        
        self.SetSizer(sizer)
        sizer.Fit(self)
        
        # binding
        self.myGrid.Bind(gridlib.EVT_GRID_SELECT_CELL, self.onSingleSelect)
        self.Bind(wx.EVT_BUTTON, self.commit, self.comBtn)
        self.Bind(wx.EVT_BUTTON, self.uncommit, self.uncomBtn)
        self.Bind(wx.EVT_BUTTON, self.makeChange, self.applyBtn)
        
        # properties
        self.comBtn.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.comBtn.SetForegroundColour('#49a03b')
        self.uncomBtn.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.uncomBtn.SetForegroundColour('#4f4dcf')
        self.applyBtn.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.applyBtn.SetForegroundColour('#ff3f15')
        self.comBtn.Disable()
        self.uncomBtn.Disable()
        self.applyBtn.Disable()
        
    #-------------------------------------------------------------------#
    def commit(self, event):
        
        row = self.currentlySelectedCell[0]
        col = self.currentlySelectedCell[1]
        val = self.myGrid.GetCellValue(row,col)
        
        dlg = wx.TextEntryDialog(self, 'Insert a new string:',
                                 "Change cell value",val,
                                 style=wx.TE_MULTILINE|wx.OK|wx.CANCEL
                                 )
        choices = ["All Present","Student is absent",
                   "Teacher is absent"
                   ]
        choiceDlg = wx.SingleChoiceDialog(self, "Change Attendance", 
                                          "Choices",choices
                                          )
        if self.rowEdit is None or self.rowEdit == row:
            if col == 0 or col == 1:
                wx.MessageBox("This column can not be changed", 
                'Change Not Allowed', wx.ICON_EXCLAMATION, self)
                return
            
            for n in range(15):
                a = self.myGrid.GetCellValue(row, n)
                self.commLast.append(a)
            
            if col == 2:
                if choiceDlg.ShowModal() == wx.ID_OK:
                    ret = choiceDlg.GetStringSelection()
                    dlg.Destroy()
                else:
                    return
            else:
                if dlg.ShowModal() == wx.ID_OK:
                    ret = dlg.GetValue()
                    dlg.Destroy()
                else:
                    return
                    
            self.myGrid.SetCellValue(row , col, ret)
            for n in range(15):
                a = self.myGrid.GetCellValue(row, n)
                self.commNew.append(a)
                
            self.myGrid.SelectRow(row, addToSelected=True)
            self.rowEdit = row
            self.uncomBtn.Enable()
            self.applyBtn.Enable()
            print self.commNew
        else:
            msg = ("Before to edit cells in others rows you must\n"
                   "push  'Apply Commit' button for render changes\n"
                   "into the columns marked in red.\n\n"
                   "Instead, if you want to remove any change push\n"
                   "'Uncommit Last' button")
            wx.MessageBox(msg, 'Change Not Allowed', wx.ICON_EXCLAMATION, self)
    #----------------------------------------------------------------------
    def uncommit(self, event):
        """
        Reprise last change and reset attributes
        """
        for n, item in enumerate(self.commLast):
            self.myGrid.SetCellValue(self.rowEdit , n, self.commLast[n])
            
        self.comBtn.Disable()
        self.uncomBtn.Disable()
        self.applyBtn.Disable()
        self.rowEdit = None
        self.commNew = []
        self.commLast = []
    #----------------------------------------------------------------------
    def makeChange(self, event):
        
        self.comBtn.Disable()
        self.uncomBtn.Disable()
        self.applyBtn.Disable()
        
        self.rowEdit = None
        self.commNew = []
        self.commLast = []
        #----------------------------------------------------------------------
    
    def onSingleSelect(self, event):
        """
        Get the selection of a single cell by clicking or 
        moving the selection with the arrow keys
        """
        self.currentlySelectedCell = (event.GetRow(),
                                    event.GetCol())
        #if self.myGrid.GetGridCursorRow() >= self.index:
        if event.GetRow() >= self.index:
            self.comBtn.Disable()
            return
        else:
            self.comBtn.Enable()
        event.Skip()
    #----------------------------------------------------------------------
    def setting(self):
        lessons = School_Class().showInTable(self.IDclass, self.path_db)

        for n, item in enumerate(lessons):
            #self.myGrid.AppendRows(n, updateLabels=False)
            self.index += 1
            #------------IDlesson
            self.myGrid.SetCellValue(n , 0, str(item[0]))
            self.myGrid.SetCellAlignment(n, 0, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
            #------------IDclass
            self.myGrid.SetCellValue(n , 1, str(item[1])) # IDclass
            self.myGrid.SetCellAlignment(n, 1, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
            #------------attendances
            self.myGrid.SetCellValue(n , 2, item[2])
            if item[2] == 'All Present':
                self.myGrid.SetCellTextColour(n, 2, '#516c1a')
            elif item[2] == 'Student is absent':
                self.myGrid.SetCellTextColour(n, 2, wx.RED)
            elif item[2] == 'Teacher is absent':
                self.myGrid.SetCellTextColour(n, 2, '#e1cf37')
            self.myGrid.SetCellFont(n, 2, wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
            self.myGrid.SetCellAlignment(n, 2, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
            #-----------date
            self.myGrid.SetCellValue(n , 3, item[3])# date
            self.myGrid.SetCellBackgroundColour(n, 3, '#deffb4')
            #-----------
            
            if item[4] == 'NONE':
                self.myGrid.SetCellValue(n, 4, '')
            else:
                self.myGrid.SetCellValue(n , 4, item[4]) # reading
            
            if item[5] == 'NONE':
                self.myGrid.SetCellValue(n, 5, '')
            else:
                self.myGrid.SetCellValue(n , 5, item[5]) # setting
                
            if item[6] == 'NONE':
                self.myGrid.SetCellValue(n, 6, '')
            else:
                self.myGrid.SetCellValue(n , 6, item[6]) # rudiments
                
            if item[7] == 'NONE':
                self.myGrid.SetCellValue(n, 7, '')
            else:
                self.myGrid.SetCellValue(n , 7, item[7]) # coordination
                
            if item[8] == 'NONE':
                self.myGrid.SetCellValue(n, 8, '')
            else:
                self.myGrid.SetCellValue(n , 8, item[8]) # styles
                
            if item[9] == 'NONE':
                self.myGrid.SetCellValue(n, 9, '')
            else:
                self.myGrid.SetCellValue(n , 9, item[9]) # minusone
                
            if item[10] == 'NONE':
                self.myGrid.SetCellValue(n, 10, '')
            else:
                self.myGrid.SetCellValue(n , 10, item[10]) # other1
                
            if item[11] == 'NONE':
                self.myGrid.SetCellValue(n, 11, '')
            else:
                self.myGrid.SetCellValue(n , 11, item[11]) # other2
                
            self.myGrid.SetCellValue(n , 12, item[12]) # other3
            if item[12] == 'NONE':
                self.myGrid.SetCellValue(n, 12, '')
                
            if item[13] == 'NONE':
                self.myGrid.SetCellValue(n, 13, '')
            else:
                self.myGrid.SetCellValue(n , 13, item[13]) # votes
                
            if item[14] == 'NONE':
                self.myGrid.SetCellValue(n , 14, '')
            else:
                self.myGrid.SetCellValue(n , 14, item[14]) # notes
            self.myGrid.SetCellBackgroundColour(n, 14, '#fffa9a')
            
        self.myGrid.AutoSizeColumns(setAsMin=True) # resize all columns
        self.myGrid.AutoSizeRows(setAsMin=True) # resize all rows
        
        
        
