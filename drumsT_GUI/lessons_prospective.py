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
        wx.Panel.__init__(self, parent, -1, style=wx.TAB_TRAVERSAL)
        
        lessons = School_Class().showInTable(IDclass, path_db)

        myGrid = gridlib.Grid(self)
        myGrid.EnableEditing(False)
        myGrid.CreateGrid(200, 6)
        myGrid.SetColLabelValue(0, "ID class")
        myGrid.SetColLabelValue(1, "Name/Surname")
        myGrid.SetColLabelValue(2, "Attendaces")
        myGrid.SetColLabelValue(3, "Lesson Date")
        myGrid.SetColLabelValue(4, "Note")
        myGrid.SetColLabelValue(5, "Votes")
        myGrid.AutoSizeColLabelSize(1)
        myGrid.AutoSizeColLabelSize(2)
        myGrid.AutoSizeColLabelSize(3)
        
        for n, item in enumerate(lessons):
            #print n, item[0]
            myGrid.SetCellValue(n , 0, str(item[1])) # id
            myGrid.SetCellAlignment(n, 0, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
            myGrid.SetCellFont(n, 0, wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
            myGrid.SetCellValue(n , 1, nameSur) # name
            myGrid.SetCellBackgroundColour(n, 1, '#deffb4')
            myGrid.SetCellValue(n , 2, item[2]) # presences
            myGrid.SetCellTextColour(n, 2, wx.RED)
            myGrid.SetCellValue(n , 3, item[3])# date
            myGrid.SetCellValue(n , 4, item[14]) # note
            myGrid.SetCellValue(n , 5, item[13]) # votes

        myGrid.AutoSizeColumns(setAsMin=True) # resize all columns
        myGrid.AutoSizeRows(setAsMin=True) # resize all rows

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, 1, wx.EXPAND, 5)
        self.SetSizer(sizer)
        sizer.Fit(self)
        
