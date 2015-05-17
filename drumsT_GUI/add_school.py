#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: add_school.py
# Porpose: Add new school and school year
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Rev (00) 17/05/2015
#########################################################

import wx

class AddSchool(wx.Dialog):
    """
    Show a dialog window.
    """
    def __init__(self, parent, title):
        """
        Mask dialog for add new school and school year
        """
        wx.Dialog.__init__(self, parent, -1, title, style=wx.DEFAULT_DIALOG_STYLE)
        
        #parent.Hide()

        #lab_top = wx.StaticText(self, wx.ID_ANY, ("Type school name or location identifier"))
        #self.txt_name = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        #lab_low = wx.StaticText(self, wx.ID_ANY, ("Add a school year:"))
        
        #self.spinctrl_year = wx.SpinCtrl(self, wx.ID_ANY, "", min=2010, max=2030, 
                                         #initial=2015, style=wx.TE_PROCESS_ENTER
                                         #)
        #lab_med = wx.StaticText(self, wx.ID_ANY, ("Dovrebbe"))
        #close_btn = wx.Button(self, wx.ID_EXIT, "")
        #apply_btn = wx.Button(self, wx.ID_OK, "Apply")

        #self.SetTitle("dialog_1")
        #self.txt_name.SetMinSize((250, 20))
        #self.txt_name.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        #self.spinctrl_year.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, 
                                            #wx.BOLD, 0, ""))

        #siz_base = wx.FlexGridSizer(5, 1, 0, 0)
        #siz_1 = wx.GridSizer(1, 3, 0, 0)
        #siz_2 = wx.GridSizer(1, 2, 0, 0)
        #siz_base.Add(lab_top, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        #siz_base.Add(self.txt_name, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        #siz_base.Add(lab_low, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        #siz_base.Add(siz_2)
        
        #siz_2.Add(self.spinctrl_year, 0, wx.ALIGN_RIGHT | wx.ALL, 15)
        #siz_2.Add(lab_med, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        
        
        #siz_1.Add(close_btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        #siz_1.Add((100, 20), 0, wx.ALIGN_CENTER | wx.ALL, 5)
        #siz_1.Add(apply_btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        #siz_base.Add(siz_1, 1, 0, 0)
        #self.SetSizer(siz_base)
        #siz_base.Fit(self)
        #self.Layout()
        

        self.label_1 = wx.StaticText(self, wx.ID_ANY, ("Type school name or location identifier:"))
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_2 = wx.StaticText(self, wx.ID_ANY, ("Add a school year:"))
        self.spin_ctrl_1 = wx.SpinCtrl(self, wx.ID_ANY, "", min=2010, max=2030, 
                                                  initial=2015, style=wx.TE_PROCESS_ENTER
                                                  )
        self.label_3 = wx.StaticText(self, wx.ID_ANY, (" /     2016"))
        self.button_2 = wx.Button(self, wx.ID_EXIT, "")
        self.button_1 = wx.Button(self, wx.ID_APPLY, "")
        
        self.SetTitle("dialog_1")
        self.text_ctrl_1.SetMinSize((250, 20))
        self.text_ctrl_1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.spin_ctrl_1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.label_3.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        
        grid_sizer_1 = wx.FlexGridSizer(5, 1, 0, 0)
        grid_sizer_2 = wx.GridSizer(1, 3, 0, 0)
        grid_sizer_3 = wx.FlexGridSizer(1, 4, 0, 0)
        grid_sizer_1.Add(self.label_1, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        grid_sizer_1.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        grid_sizer_1.Add(self.label_2, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        grid_sizer_3.Add((45, 20), 0, wx.ALIGN_CENTER | wx.ALL, 15)
        grid_sizer_3.Add(self.spin_ctrl_1, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        grid_sizer_3.Add(self.label_3, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        grid_sizer_1.Add(grid_sizer_3, 1, 0, 0)
        grid_sizer_2.Add(self.button_2, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        grid_sizer_2.Add((100, 20), 0, wx.ALIGN_CENTER | wx.ALL, 15)
        grid_sizer_2.Add(self.button_1, 0, wx.ALIGN_CENTER | wx.ALL, 15)
        grid_sizer_1.Add(grid_sizer_2, 1, 0, 0)
        self.SetSizer(grid_sizer_1)
        grid_sizer_1.Fit(self)
        self.Layout()
        
        
        #self.Bind(wx.EVT_CLOSE, self.on_close)
        #self.Bind(wx.EVT_BUTTON, self.on_close, close_btn)
        #self.Bind(wx.EVT_BUTTON, self.on_apply, apply_btn)
        
    #def sel_year(self, event):
        
        
    def on_close(self, event):
        self.Destroy()
        event.Skip()
        
    def on_apply(self, event):
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
        event.Skip()
        
    def GetValue(self):
        name = self.txt_name.GetValue()
        year = self.spinctrl_year.GetValue()
        print 'value', name, year
        
        return name
        

