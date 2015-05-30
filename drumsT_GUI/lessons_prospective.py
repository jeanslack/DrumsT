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

        myGrid = gridlib.Grid(self)
        myGrid.EnableEditing(False) # make all in read only
        myGrid.CreateGrid(150, 15)
        myGrid.SetColLabelValue(0, "ID lesson")
        myGrid.SetColLabelValue(1, "ID class")
        myGrid.SetColLabelValue(2, "Attendances")
        myGrid.SetColLabelValue(3, "Lesson Date")
        myGrid.SetColLabelValue(4, "Chart Reading")
        myGrid.SetColLabelValue(5, "Hands/foots Setting")
        myGrid.SetColLabelValue(6, "Rudiments")
        myGrid.SetColLabelValue(7, "Coordination")
        myGrid.SetColLabelValue(8, "Styles")
        myGrid.SetColLabelValue(9, "Minus One")
        myGrid.SetColLabelValue(10, "Other-1")
        myGrid.SetColLabelValue(11, "Other-2")
        myGrid.SetColLabelValue(12, "Other-3")
        myGrid.SetColLabelValue(13, "Votes")
        myGrid.SetColLabelValue(14, "Note/Reminder")
        #### set columns 0-1-2 in read only
        #attr = gridlib.GridCellAttr()
        #attr.SetReadOnly(True)
        #myGrid.SetColAttr(0, attr)
        #myGrid.SetColAttr(1, attr)
        #myGrid.SetColAttr(2, attr)
        ## oppure: myGrid.SetReadOnly(3, 3, True)
        lessons = School_Class().showInTable(IDclass, path_db)

        for n, item in enumerate(lessons):
            #------------IDlesson
            myGrid.SetCellValue(n , 0, str(item[0]))
            myGrid.SetCellAlignment(n, 0, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
            #------------IDclass
            myGrid.SetCellValue(n , 1, str(item[1])) # IDclass
            myGrid.SetCellAlignment(n, 1, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
            #------------attendances
            myGrid.SetCellValue(n , 2, item[2])
            if item[2] == 'All Present':
                myGrid.SetCellTextColour(n, 2, '#516c1a')
            elif item[2] == 'Student is absent':
                myGrid.SetCellTextColour(n, 2, wx.RED)
            elif item[2] == 'Teacher is absent':
                myGrid.SetCellTextColour(n, 2, '#e1cf37')
            myGrid.SetCellFont(n, 2, wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD))
            myGrid.SetCellAlignment(n, 2, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
            #-----------date
            myGrid.SetCellValue(n , 3, item[3])# date
            myGrid.SetCellBackgroundColour(n, 3, '#deffb4')
            #-----------
            myGrid.SetCellValue(n , 4, item[4]) # reading
            if item[4] == 'NONE':
                myGrid.SetCellValue(n, 4, '')
            
            myGrid.SetCellValue(n , 5, item[5]) # setting
            if item[5] == 'NONE':
                myGrid.SetCellValue(n, 5, '')
                
            myGrid.SetCellValue(n , 6, item[6]) # rudiments
            if item[6] == 'NONE':
                myGrid.SetCellValue(n, 6, '')
                
            myGrid.SetCellValue(n , 7, item[7]) # coordination
            if item[7] == 'NONE':
                myGrid.SetCellValue(n, 7, '')
                
            myGrid.SetCellValue(n , 8, item[8]) # styles
            if item[8] == 'NONE':
                myGrid.SetCellValue(n, 8, '')
                
            myGrid.SetCellValue(n , 9, item[9]) # minusone
            if item[9] == 'NONE':
                myGrid.SetCellValue(n, 9, '')
                
            myGrid.SetCellValue(n , 10, item[10]) # other1
            if item[10] == 'NONE':
                myGrid.SetCellValue(n, 10, '')
                
            myGrid.SetCellValue(n , 11, item[11]) # other2
            if item[11] == 'NONE':
                myGrid.SetCellValue(n, 11, '')
                
            myGrid.SetCellValue(n , 12, item[12]) # other3
            if item[12] == 'NONE':
                myGrid.SetCellValue(n, 12, '')
                
            myGrid.SetCellValue(n , 13, item[13]) # votes
            if item[13] == 'NONE':
                myGrid.SetCellValue(n, 13, '')
                
            myGrid.SetCellValue(n , 14, item[14]) # notes
            if item[14] == 'NONE':
                myGrid.SetCellValue(n , 14, '')
            myGrid.SetCellBackgroundColour(n, 14, '#fffa9a')

        myGrid.AutoSizeColumns(setAsMin=True) # resize all columns
        myGrid.AutoSizeRows(setAsMin=True) # resize all rows

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, 1, wx.EXPAND, 5)
        self.SetSizer(sizer)
        sizer.Fit(self)
        
