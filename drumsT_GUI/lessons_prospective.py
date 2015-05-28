#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: lesson_prospective.py
# Porpose: Show a data list of all lessons
# Author: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (00) 28/05/2015
#########################################################

import wx
import wx.grid as  gridlib

class PanelTwo(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.TAB_TRAVERSAL)
        myGrid = gridlib.Grid(self)
        myGrid.CreateGrid(365, 6)
        
        myGrid.SetCellValue(0,0, "Hello")
        myGrid.SetCellFont(0, 0, wx.Font(12, wx.ROMAN, wx.ITALIC, wx.NORMAL))
        #print myGrid.GetCellValue(0,0)
        
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
        
