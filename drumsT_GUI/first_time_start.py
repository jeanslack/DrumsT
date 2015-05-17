#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: first_time_start.py
# Porpose: Show when there is not nothing database
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (00) 16/05/2015
#########################################################
#
import wx
from add_school import AddSchool
class MyDialog(wx.Dialog):
    
    def __init__(self, img):
        
        self.path_db = wx.GetApp().path_db
        
        wx.Dialog.__init__(self, None, -1, style=wx.DEFAULT_DIALOG_STYLE)
        bitmap_drumsT = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(img, 
                                                           wx.BITMAP_TYPE_ANY)
        )
        msg = ("Questa e la prima volta vhe avviate DrumsT.\n\n"
               "DrumsT e un gestionale scolastico indicato per gli "
               "insegnanti di batteria.\n\n"
               "- Se vuoi creare ora un nuovo database premi il pulsante "
               "Crea.\n\n- Se vuoi importarne uno di esistente premi il "
               "pulsante importa.\n\n- Premi esci per uscire semplicemente")
        lab_welc2 = wx.StaticText(self, wx.ID_ANY, (msg))
        lab_welc1 = wx.StaticText(self, wx.ID_ANY, ("Benvenuti !"))
        lab_create = wx.StaticText(self, wx.ID_ANY, ("Creare un nuovo database:"))
        lab_import = wx.StaticText(self, wx.ID_ANY, ("Importa un database di back-up:"))
        lab_exit = wx.StaticText(self, wx.ID_ANY, ("Esci e non fare niente:"))
        create_btn = wx.Button(self, wx.ID_ANY, ("Crea"))
        import_btn = wx.Button(self, wx.ID_ANY, ("Importa"))
        close_btn = wx.Button(self, wx.ID_EXIT, "")
        
        self.SetTitle("DrumsT")
        lab_welc1.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, 
                                              wx.BOLD, 0, ""))
        
        grd_base = wx.GridSizer(2, 1, 0, 0)
        grd_1 = wx.FlexGridSizer(1, 2, 0, 0)
        grd_ext = wx.FlexGridSizer(2, 1, 0, 0)
        grd_2 = wx.FlexGridSizer(3, 2, 0, 0)
        grd_base.Add(grd_1)
        grd_1.Add(bitmap_drumsT,0,wx.ALL, 15)
        grd_1.Add(grd_ext)
        grd_base.Add(grd_2)
        grd_ext.Add(lab_welc1,0,  wx.ALL, 15)
        grd_ext.Add(lab_welc2,0, wx.ALIGN_CENTER | wx.ALL, 15)
        grd_2.Add(lab_create,0, wx.ALIGN_CENTER | wx.ALL, 15)
        grd_2.Add(create_btn,0, wx.ALIGN_CENTER | wx.ALL, 15)
        grd_2.Add(lab_import,0, wx.ALIGN_CENTER | wx.ALL, 15)
        grd_2.Add(import_btn,0, wx.ALIGN_CENTER | wx.ALL, 15)
        grd_2.Add(lab_exit,0, wx.ALIGN_CENTER | wx.ALL, 15)
        grd_2.Add(close_btn,0, wx.ALIGN_CENTER | wx.ALL, 15)
        self.SetSizer(grd_base)
        grd_base.Fit(self)
        self.Layout()
        
        self.Bind(wx.EVT_BUTTON, self.on_close)
        self.Bind(wx.EVT_BUTTON, self.create_now, create_btn)
        self.Bind(wx.EVT_BUTTON, self.import_now, import_btn)
        
        
    def on_close(self, event):
        self.Destroy()
        
    def create_now(self, event):
        dialog = AddSchool(self, "Add new identity profile to database")
        retcode = dialog.ShowModal()
        #ret = dialog.ShowModal()
        if retcode == wx.ID_OK:
            data = dialog.GetValue()
            print 'ritorno', data
        
    def import_now(self, event):
        print 'importare'
