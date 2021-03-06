#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: add_newyear.py
# Porpose: Add a new year to selected school
# Author: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (00) 15/05/2015
#########################################################
#
import wx

class AddYear(wx.Dialog):
    """
    Show a dialog window for return new school year data
    """
    def __init__(self, parent, title):
        """
        """
        wx.Dialog.__init__(self, parent, -1, title, style=wx.DEFAULT_DIALOG_STYLE)
        
        # set attributes
        self.parent = parent
        self.max_year = '2016'
        self.min_year = '2015'
        # widgets:
        labmsg = wx.StaticText(self, wx.ID_ANY, (
                                    "Add a school year to selected school:")
        )
        self.spinctrl_year = wx.SpinCtrl(self, wx.ID_ANY, "", min=2010, max=2030, 
                                       initial=2015, style=wx.TE_PROCESS_ENTER
                                       )
        self.labyear = wx.StaticText(self, wx.ID_ANY, ("  /      2016"))
        close_btn = wx.Button(self, wx.ID_EXIT, "")
        apply_btn = wx.Button(self, wx.ID_OK, "")
        # properties:
        self.spinctrl_year.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.labyear.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        # layout:
        gridbase = wx.FlexGridSizer(3, 1, 0, 0)
        gridsiz1 = wx.GridSizer(1, 3, 0, 0)
        gridsiz2 = wx.FlexGridSizer(1, 4, 0, 0)
        gridbase.Add(labmsg, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        gridsiz2.Add((60, 20), 0, wx.ALIGN_CENTER | wx.ALL, 15)
        gridsiz2.Add(self.spinctrl_year, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        gridsiz2.Add(self.labyear, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        gridbase.Add(gridsiz2, 1, 0, 0)
        gridsiz1.Add(close_btn, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        gridsiz1.Add((100, 20), 0, wx.ALIGN_CENTER | wx.ALL, 15)
        gridsiz1.Add(apply_btn, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        gridbase.Add(gridsiz1, 1, 0, 0)
        self.SetSizer(gridbase)
        gridbase.Fit(self)
        self.Layout()
        # bindings:
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Bind(wx.EVT_BUTTON, self.on_close, close_btn)
        self.Bind(wx.EVT_SPINCTRL, self.enter_year, self.spinctrl_year)
    #-------------------------------------------------------------------#
    def enter_year(self, event):
        """
        Apply a confortable reading for school years.
        Also set self.min_year and self.max_year attributes
        """
        self.min_year = self.spinctrl_year.GetValue()
        y = int(self.min_year) + 1
        self.max_year = str(y)
        self.labyear.SetLabel("  /      %s" % self.max_year)
        #self.sizer.Layout() # use it if the change layout too
    #-------------------------------------------------------------------#
    def on_close(self, event):
        #self.parent.Show()
        self.Destroy()
        #event.Skip()
    #-------------------------------------------------------------------#
    #def on_apply(self, event):
        """
        pass event to self.GetValue()
        """
        #if you enable self.Destroy(), it delete from memory all data 
        #event and no return correctly. It has the right behavior if 
        #not used here, because it is called in the main frame. 
        #self.Destroy()
        
        #self.GetValue(), is completely useless here because back two times 
        
        #Event.Skip(), work correctly here. Sometimes needs to disable 
        #it for needs to maintain the view of the window (for exemple).
        #event.Skip()
    #-------------------------------------------------------------------#
    def GetValue(self):
        """
        Return by call before Destroy()
        """

        setyear = '%s/%s' % (self.min_year,self.max_year)
        return setyear
    
