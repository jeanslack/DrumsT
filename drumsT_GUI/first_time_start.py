#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: first_time_start.py
# Porpose: Showing when there is not nothing database
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (00) 16/05/2015
#########################################################
#
import wx
from add_school import AddSchool
from drumsT_SYS.data_schools import Schools_Id
from drumsT_SYS.data_students import Students_Id
from drumsT_SYS.os_proc import write_newpath, create_rootdir

#from drumsT_SYS.data_schools import Schools_Id
#from drumsT_SYS.boot import write_fileconf
class FirstStart(wx.Dialog):
    
    def __init__(self, img):
        
        self.path_db = wx.GetApp().path_db
        
        wx.Dialog.__init__(self, None, -1, style=wx.DEFAULT_DIALOG_STYLE)
        
        # variables or attributes:
        msg = ("This is the first time you start DrumsT.\n\n"
               "DrumsT is a management school designed for drums teachers.\n\n"
               "- If you want to create a new database now press the "
               "create button.\n\n- If a database already exists press "
               "the import button.\n\n- Press the exit button to exit simply")
        
        # widget:
        bitmap_drumsT = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(
            img,wx.BITMAP_TYPE_ANY))
        lab_welc2 = wx.StaticText(self, wx.ID_ANY, (msg))
        lab_welc1 = wx.StaticText(self, wx.ID_ANY, ("Welcome !"))
        lab_create = wx.StaticText(self, wx.ID_ANY, ("Create a new database:"))
        lab_import = wx.StaticText(self, wx.ID_ANY, ("Show me an existing database:"))
        lab_exit = wx.StaticText(self, wx.ID_ANY, ("Exit and do nothing:"))
        create_btn = wx.Button(self, wx.ID_ANY, ("Create"))
        import_btn = wx.Button(self, wx.ID_ANY, ("Import"))
        close_btn = wx.Button(self, wx.ID_EXIT, "")
        
        # properties
        self.SetTitle("DrumsT")
        lab_welc1.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL,wx.BOLD, 0, ""))
        # layout:
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
        
        ######################## bindings #####################
        self.Bind(wx.EVT_BUTTON, self.on_close)
        self.Bind(wx.EVT_BUTTON, self.create_now, create_btn)
        self.Bind(wx.EVT_BUTTON, self.import_now, import_btn)
        
    # EVENTS:
    #-------------------------------------------------------------------#
    def on_close(self, event):
        self.Destroy()
    #-------------------------------------------------------------------#
    def create_now(self, event):
        """
        Create new 
        """
        dialog = AddSchool(self, "DrumsT - create new database school")
        retcode = dialog.ShowModal()

        if retcode == wx.ID_OK:
            data = dialog.GetValue()
        else:
            wx.MessageBox("You could not set anything", 
                          'Warning', wx.ICON_EXCLAMATION, self)
            return
        
        dialogdir = wx.DirDialog(self, "Where do you want to save ?")
        
        if dialogdir.ShowModal() == wx.ID_OK:
            path = dialogdir.GetPath()
            rootpath = "%s/DrumsT_DataBases" % path
            dialogdir.Destroy()
            
            mkdirs = create_rootdir(rootpath,data[0],data[1])
            if mkdirs[0]:
                wx.MessageBox(mkdirs[1], 'ERROR', wx.ICON_ERROR, self)
                return

            schools = Schools_Id().first_start(path,data[0],data[1])
            if schools[0]:
                wx.MessageBox(schools[1], 'ERROR', wx.ICON_ERROR, self)
                return
            
            students = Students_Id().first_start(rootpath,data[0],data[1])
            if students[0]:
                wx.MessageBox(students[1], 'ERROR', wx.ICON_ERROR, self)
                return
            
            write_newpath('%s/DrumsT_DataBases' % path) # writing drumsT.conf
            
            wx.MessageBox("A new database has been created successfully in:"
                          "\n\n%s/DrumsT_Databases\n\nYou must re-start the "
                          "DrumsT application now.\n\nGood Work !" % path, 
                          'Success !', wx.ICON_INFORMATION, self)
            self.Destroy()
        else:
            wx.MessageBox("You could not set anything", 'Warning', 
                          wx.ICON_EXCLAMATION, self)
            return
    #-------------------------------------------------------------------#
    def import_now(self, event):
        
        dialdir = wx.DirDialog(self, "Where is the database folder "
                                     "'DrumsT_DataBases' ?"
                                     )
        if dialdir.ShowModal() == wx.ID_OK:
            path = dialdir.GetPath()
            dialdir.Destroy()
            
            write_newpath(path)
            wx.MessageBox("A database has been imported successfully in:"
                          "\n\n%s\n\nYou must re-start the "
                          "DrumsT application now.\n\nGood Work !" % path, 
                          'Success !', wx.ICON_INFORMATION, self)
            self.Destroy()
        else:
            wx.MessageBox("You could not set anything", 
                          'Warning', wx.ICON_EXCLAMATION, self)
            return
