#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: on_init.py
# Porpose: bootstrap with application system controls
# Author: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (00) 15/05/2015
#########################################################
#
import wx
from drumsT_SYS.boot import control_config, parser_fileconf, rootdirControl

class DrumsTeacher(wx.App):
    """
    This is a bootstrap interface that is needed to do 
    application initialization to ensure that the system, 
    toolkit and wxWidgets are fully initialized.
    """
    def __init__(self, redirect=True, filename=None):
        """
        Creating attributes that will be used after in other class
        with GetApp()
        """
        print "App __init__"
        ctrl = control_config() #system control
        self.drumsT_icon = ctrl[0]
        self.openStudent_icon = ctrl[1]
        self.addStudent_icon = ctrl[2]
        self.changeStudent_icon = ctrl[3]
        self.delStudent_icon = ctrl[4]
        self.OS = ctrl[5]
        self.main_path = ctrl[6]
        self.copyerr = ctrl[7]
        self.tab_icon = ctrl[8]
        self.lesson_icon = ctrl[9]
        wx.App.__init__(self, redirect, filename) # Call the base class constructor
        
    def OnInit(self):
        """
        Determine if everything works: return True
        or if something is wrong: return False
        """
        
        if self.copyerr: # if source dir is corrupt
            message = ("Can not find the configuration file. "
                       "Please, reinstall the drumsT application")
            print "DrumsT: Fatal Error, %s" % message
            wx.MessageBox(message, 'drumsT: Fatal Error', wx.ICON_STOP)
            return False
        
        #---------------------Parsing file-conf-------------------------#
        conf = parser_fileconf() #parsing drumsT.conf
        self.rootdir = conf
        
        if self.rootdir == 'empty': # not set
            self.reprise()
            return True
        
        elif self.rootdir == 'error': # is corrupt
            message = ("The configuration file is wrong. "
                       "Please, reinstall the drumsT application")
            print "DrumsT: Fatal Error, %s" % message
            wx.MessageBox(message, 'DrumsT: Fatal Error', wx.ICON_STOP)
            return False
        
        #--------------------Check paths--------------------------------#
        ret = rootdirControl(self.rootdir) #control existing 
        
        if not ret:
            message = ("The root directory for saving databases no longer\n"
                       "exists.\n\n"
                       "Do you want to provide to create another one?")
            print ("DrumsT: Warning, The root directory for saving "
                   "databases no longer exists.")
            style = wx.YES_NO | wx.CANCEL | wx.ICON_EXCLAMATION
            dlg = wx.MessageDialog(parent=None, message=message, 
                                   caption="DrumsT: Warning", style=style
                                   )
            if dlg.ShowModal() == wx.ID_YES:
                self.reprise()
                return True
            else:
                return False
       #-----------------------------------------------------------------#
        else: # run main frame
            from drumsT_GUI.mainwindow import MainFrame
            main_frame = MainFrame()
            main_frame.Show()
            self.SetTopWindow(main_frame)
            return True
        
    def reprise(self): # start a temporary dialog
        from drumsT_GUI.first_time_start import FirstStart
        main_frame = FirstStart(self.drumsT_icon)
        main_frame.Show()
        self.SetTopWindow(main_frame)
        return True
    
    def OnExit(self):
        print "OnExit"
        
    
if __name__ == "__main__":
    """
    redirect standard out to a separate window:
        app = DrumsTeacher(redirect=True)
    redirect standard out to a terminal:
        app = DrumsTeacher(False)
    If () is empty default is redirect=True:
        app = DrumsTeacher()
    If None is same at True:
        app = DrumsTeacher(None)
    """
    app = DrumsTeacher(False)
    fred = app.MainLoop()
    print "after MainLoop", fred
