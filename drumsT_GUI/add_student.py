#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: add_student.py
# Porpose: students profile storing dialog
# Author: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Rev (00) 16/05/2015
#########################################################

import wx

class AddRecords(wx.Dialog):
    """
    Show a dialog window.
    """
    def __init__(self, parent, title):
        """
        Mask dialog for recording new students profiles.
        """
        wx.Dialog.__init__(self, parent, -1, title, style=wx.DEFAULT_DIALOG_STYLE)
        self.listret = []
        # widgets:
        siz_name = wx.StaticBox(self, wx.ID_ANY, "  Name:")
        siz_surname = wx.StaticBox(self, wx.ID_ANY, "  Surname:")
        siz_phone = wx.StaticBox(self, wx.ID_ANY, "  Phone:")
        siz_address = wx.StaticBox(self, wx.ID_ANY, "  Address:")
        siz_birth = wx.StaticBox(self, wx.ID_ANY, "  Birth-Dates:")
        siz_date = wx.StaticBox(self, wx.ID_ANY, "  Joined Date:")
        siz_level = wx.StaticBox(self, wx.ID_ANY, "  Level:")
        siz_info = wx.StaticBox(self, wx.ID_ANY, "  Others Info:")
        
        self.txt_name = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        self.txt_surname = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        self.txt_phones = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        self.txt_address = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER | wx.TE_MULTILINE)
        self.txt_birth = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        self.txt_date = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        self.txt_level = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        self.txt_info = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER)
        
        close_btn = wx.Button(self, wx.ID_CANCEL, "Close")
        #help_btn = wx.Button(self, wx.ID_HELP, "")
        ok_btn = wx.Button(self, wx.ID_OK, "") 

        # Properties:
        self.txt_name.SetMinSize((180, 30))
        self.txt_surname.SetMinSize((180, 30))
        self.txt_phones.SetMinSize((180, 30))
        self.txt_address.SetMinSize((300, 60))
        self.txt_birth.SetMinSize((180, 30))
        self.txt_date.SetMinSize((180, 30))
        self.txt_level.SetMinSize((150, 30))
        self.txt_info.SetMinSize((150, 30))
        
        # Layout:
        base = wx.FlexGridSizer(5, 2, 20, 20)
        
        box_name = wx.StaticBoxSizer(siz_name, wx.VERTICAL)
        box_name.Add(self.txt_name,0)
        
        box_surname = wx.StaticBoxSizer(siz_surname, wx.VERTICAL)
        box_surname.Add(self.txt_surname,0)
        
        box_phone = wx.StaticBoxSizer(siz_phone, wx.VERTICAL)
        box_phone.Add(self.txt_phones,0)
        
        box_address = wx.StaticBoxSizer(siz_address, wx.VERTICAL)
        box_address.Add(self.txt_address,0)
        
        box_birth = wx.StaticBoxSizer(siz_birth, wx.VERTICAL)
        box_birth.Add(self.txt_birth,0) 
        
        box_date = wx.StaticBoxSizer(siz_date, wx.VERTICAL)
        box_date.Add(self.txt_date,0)
        
        box_level = wx.StaticBoxSizer(siz_level, wx.VERTICAL)
        box_level.Add(self.txt_level,0)
        
        box_info = wx.StaticBoxSizer(siz_info, wx.VERTICAL)
        box_info.Add(self.txt_info,0)
        
        base.AddMany([(box_name, 0, wx.ALL, 15),(box_surname, 0, wx.ALL, 15),
                      (box_phone, 0, wx.ALL, 15),(box_address, 0, wx.ALL, 15),
                      (box_birth, 0,wx.ALL, 15),(box_date, 0, wx.ALL, 15),
                      (box_level, 0, wx.ALL, 15),(box_info, 0, wx.ALL, 15)]
                     )
        base.Add(close_btn, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 15)
        base.Add(ok_btn, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 15)

        self.SetSizer(base)
        base.Fit(self)
        self.Layout()

        #----------------------Binder (EVT)----------------------#
        self.Bind(wx.EVT_BUTTON, self.on_close, close_btn)
        self.Bind(wx.EVT_BUTTON, self.on_apply, ok_btn) 
        
    #---------------------Callback (event handler)----------------------#

    def on_close(self, event):
        #self.Destroy()
        event.Skip()

    def on_apply(self, event):
        """
        Apply is need to management errors before go GetValue()
        """
        name = self.txt_name.GetValue()
        surname = self.txt_surname.GetValue()
        phone = self.txt_phones.GetValue()
        address = self.txt_address.GetValue()
        birthdate = self.txt_birth.GetValue()
        date = self.txt_date.GetValue()
        level = self.txt_level.GetValue()
        
        self.listret = [name,surname,phone,address,birthdate,date,level]
        for e in self.listret:
            if e == '':
                wx.MessageBox(u"Incomplete profile assignement. Is not "
                              "still possible to save into the database !",
                              "Warning", wx.ICON_EXCLAMATION, self)
                return
            
        event.Skip()
        
    def GetValue(self):
        """
        Return by call before Destroy()
        """
        return self.listret
