#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: lessons.py
# Porpose: Frame content for panels of lessons record
# Author: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (00) 28/05/2015
#########################################################

import wx
from src.drumsT_GUI.add_lesson import PanelOne
from src.drumsT_GUI.lessons_prospective import PanelTwo

class Lesson(wx.Frame):
    """
    Implement a wx.frame window for others panels
    """
 
    def __init__(self, namesur, IDclass, path_db):
        """
        This frame has not parent (is None) and is independence from
        others windows. This is confortable for more istances of same 
        windows for more management of students
        """
        # set need attributes:
        self.drumsT_ico = wx.GetApp().drumsT_icon
        self.tab_ico = wx.GetApp().tab_icon
        self.lesson_ico = wx.GetApp().lesson_icon
        self.nameSur = namesur # name surname on title
        self.IDclass = IDclass
        self.path_db = path_db
        
        wx.Frame.__init__(self, None, -1, style=wx.DEFAULT_FRAME_STYLE)
        
        self.InitUI()
        
    def InitUI(self):
        """
        start with widgets and setup
        """
        self.tool_bar()
        
        self.panel_one = PanelOne(self, self.nameSur, self.IDclass, self.path_db)
        self.panel_two = PanelTwo(self, self.nameSur, self.IDclass, self.path_db)
        self.panel_two.Hide()
        ################### layout
        self.sizer = wx.FlexGridSizer()
        self.sizer.Add(self.panel_one, 1, wx.EXPAND|wx.ALL, 10)
        self.sizer.Add(self.panel_two, 1, wx.EXPAND|wx.ALL, 10)
        self.sizer.AddGrowableRow(0)
        self.sizer.AddGrowableCol(0)
        
        
        #################### Properties
        self.SetTitle(("Record a new lesson for %s" % self.nameSur))
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap(self.drumsT_ico, wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        
        self.SetSize((810, 580))
        self.CentreOnScreen()
        self.SetSizer(self.sizer)
        self.Layout()
        #self.Show()# for stand-alone case only
        self.toolbar.EnableTool(wx.ID_FILE2, False)
        
        ################### Binding
        self.Bind(wx.EVT_CLOSE, self.on_close)
        
    ################ event handler
    def on_close(self, event):
        self.Destroy()
        
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
        pantab = self.toolbar.AddLabelTool(wx.ID_FILE2, " Record a new lesson",
                                           wx.Bitmap(self.lesson_ico))
        self.toolbar.AddSeparator()
        
        # ------- Add new student
        panlesson = self.toolbar.AddLabelTool(wx.ID_FILE3, " Overall view" , 
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
        """
        Show a interface for record new day lesson
        """
        if self.panel_two.IsShown():
            self.SetTitle("Record a new lesson for %s" % self.nameSur)
            self.panel_one.Show()
            self.panel_two.Hide()
            self.toolbar.EnableTool(wx.ID_FILE3, True)
            self.toolbar.EnableTool(wx.ID_FILE2, False)
            self.Layout()
    #------------------------------------------------------------------#
    def panLesson(self, event):
        """
        Show a table with list of all lessons
        """
        if self.panel_one.IsShown():
            self.SetTitle("Overall view of %s" % self.nameSur)
            self.panel_one.Hide()
            self.panel_two.Show()
            self.toolbar.EnableTool(wx.ID_FILE3, False)
            self.toolbar.EnableTool(wx.ID_FILE2, True)
            self.Layout()
        
 
#if __name__ == '__main__':
    #app = wx.App(False)
    #frame = Lesson()
    #app.MainLoop()
