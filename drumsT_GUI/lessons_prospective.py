#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: lesson_prospective.py
# Porpose: Show data of all lessons of a one student
# Author: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (00) 28/05/2015
#########################################################

import wx
import wx.grid as  gridlib
from drumsT_SYS.SQLite_lib import School_Class

class PanelTwo(wx.Panel):
    """
    Show a grid with tabular data.
    It was inspired on codes from:
    http://www.blog.pythonlibrary.org/2013/10/31/wxpython-how-to-get-selected-cells-in-a-grid/
    http://www.blog.pythonlibrary.org/2010/04/04/wxpython-grid-tips-and-tricks/
    http://www.blog.pythonlibrary.org/2010/03/18/wxpython-an-introduction-to-grids/
    Official Documents:
    http://wxpython.org/Phoenix/docs/html/grid.Grid.html
    """
    def __init__(self, parent, nameSur, IDclass, path_db):
        """
        Display a list with data of all previous lessons of
        the student in object and relating to school
        year selected only 
        """
        wx.Panel.__init__(self, parent, -1, style=wx.TAB_TRAVERSAL)
        #### set attributes:
        self.currentlySelectedCell = (0, 0) # row, col default
        self.rowEdit = None # tracking what row is was edited
        self.newsEdit = [] # list of all item edited
        self.backUp = [] # last backup for recovery
        self.index = 0 # how many items (rows) 
        self.path_db = path_db
        self.IDclass = IDclass
        self.IDlesson = None
        
        self.InitUI()
        
    def InitUI(self):
        """
        Start with widget and panel setup
        """
        self.editBtn = wx.Button(self, wx.ID_ANY, ("Changes"))
        self.rollbackBtn = wx.Button(self, wx.ID_ANY, ("Rollback"))
        self.applyBtn = wx.Button(self, wx.ID_ANY, ("Apply Commit"))
        self.myGrid = gridlib.Grid(self)
        #### properties:
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
        # see above address: www.../wxpython-an-introduction-to-grids/
        #attr = gridlib.GridCellAttr()
        #attr.SetReadOnly(True)
        #self.myGrid.SetColAttr(0, attr)
        #self.myGrid.SetColAttr(1, attr)
        #self.myGrid.SetColAttr(2, attr)
        ## oppure: self.myGrid.SetReadOnly(3, 3, True)
        #### properties
        self.editBtn.SetToolTipString("Changes text or value into the "
                                     "cells and append")
        self.rollbackBtn.SetToolTipString("Rollback to the last state or first "
                                     "to the last 'Apply-Commit'")
        self.applyBtn.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.applyBtn.SetForegroundColour('#ff3f15')
        self.applyBtn.SetToolTipString("Make an update and commit new "
                                       "changes into database")
        self.editBtn.Disable()
        self.rollbackBtn.Disable()
        self.applyBtn.Disable()
        #### go to popular the grid:
        self.setting()
        #### Build Layout:
        sizer = wx.BoxSizer(wx.VERTICAL)
        gridSiz = wx.GridSizer(1,3,0,40)
        sizer.Add(self.myGrid, 1, wx.EXPAND, 5)
        sizer.Add(gridSiz, 0, wx.ALL, 5)
        gridSiz.Add(self.editBtn, 0, wx.ALL, 5)
        gridSiz.Add(self.rollbackBtn, 0, wx.ALL, 5)
        gridSiz.Add(self.applyBtn, 0, wx.ALL, 5)
        self.SetSizer(sizer)
        sizer.Fit(self)
        #### binding
        self.myGrid.Bind(gridlib.EVT_GRID_SELECT_CELL, self.onSingleSelect)
        self.Bind(wx.EVT_BUTTON, self.editCells, self.editBtn)
        self.Bind(wx.EVT_BUTTON, self.restroreLast, self.rollbackBtn)
        self.Bind(wx.EVT_BUTTON, self.makeChange, self.applyBtn)
    #-------------------------
    def setting(self):
        """
        Set properties and set the grid cells with values
        of the query.
        """
        lessons = School_Class().showInTable(self.IDclass, self.path_db)
        for n, item in enumerate(lessons):
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
    #--------------------------------------------------------------------#
    #--------------------------------EVENT-------------------------------#
    def editCells(self, event):
        """
        Make editable the columns in the row where the 
        cell is selected only
        """
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
            
            if self.IDlesson not in self.backUp:
                del self.backUp[:] # first clear list
                for n in range(15):
                    i = self.myGrid.GetCellValue(row, n)
                    self.backUp.append(i)
            
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
            
            del self.newsEdit[:] # first clear list 
            for n in range(15):
                i = self.myGrid.GetCellValue(row, n)
                self.newsEdit.append(i)
                
            self.rowEdit = row
            self.rollbackBtn.Enable()
            self.applyBtn.Enable()
        else:
            msg = ("Before to edit cells in others rows, you must\n"
                   "push  'Apply Commit' button for render changes\n"
                   "into the edited columns selected in gray.\n\n"
                   "Instead, if you want to remove any change push\n"
                   "'Uncommit Last' button")
            self.myGrid.SelectRow(self.rowEdit, addToSelected=True)
            wx.MessageBox(msg, 'Change Not Allowed', wx.ICON_EXCLAMATION, self)
    #----------------------------------------------------------------------
    def restroreLast(self, event):
        """
        Retrieve last change and reset attributes. The data 
        retrieving of previous setting it is restored. 
        WARNING: this not restore after a apply-commit
        """
        for n, item in enumerate(self.backUp):
            self.myGrid.SetCellValue(self.rowEdit , n, self.backUp[n])
        self.editBtn.Disable()
        self.rollbackBtn.Disable()
        self.applyBtn.Disable()
        self.rowEdit = None
        del self.newsEdit[:]
        del self.backUp[:]
        self.IDlesson = None
    #----------------------------------------------------------------------
    def makeChange(self, event):
        """
        Allow to save changes in db (table Lesson) 
        """
        for n, item in enumerate(self.newsEdit):# if empty str fill out with NONE str
            if item.strip() == '':
                self.newsEdit[n] = 'NONE'
                
        change = School_Class().change_lesson_items(self.newsEdit, self.path_db)
        
        if change[0]:
            wx.MessageBox(change[1], 'Error', wx.ICON_ERROR, self)
            return
        
        self.editBtn.Disable()
        self.rollbackBtn.Disable()
        self.applyBtn.Disable()
        self.rowEdit = None
        del self.newsEdit[:]
        del self.backUp[:]
        self.IDlesson = None
        
        self.index = 0 
        self.setting()
        wx.MessageBox("Successfull storing !", "Success", wx.OK, self)
        #----------------------------------------------------------------------
    def onSingleSelect(self, event):
        """
        Get the selection of a single cell by clicking or 
        moving the selection with the arrow keys
        """
        self.currentlySelectedCell = (event.GetRow(),
                                    event.GetCol())
        self.IDlesson = self.myGrid.GetCellValue(self.currentlySelectedCell[0], 
                                                 0)
        if event.GetRow() >= self.index:
            self.editBtn.Disable()
            return
        else:
            self.editBtn.Enable()
        event.Skip()
    #----------------------------------------------------------------------
    
