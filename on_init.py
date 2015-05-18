#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: on_init.py
# Porpose: bootstrap with application system controls
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (00) 15/05/2015
#########################################################
#
import wx
from drumsT_SYS.boot import control_config, parser_fileconf, control_db

class DrumsTeacher(wx.App):
    """
    This is a bootstrap interface
    """
    def OnInit(self):
        """
        Main initilize ctrl
        """
        #----------------------Main assignements------------------------#
        ctrl = control_config() #system control
        self.drumsT_icon = ctrl[0]
        self.openStudent_icon = ctrl[1]
        self.addStudent_icon = ctrl[2]
        self.changeStudent_icon = ctrl[3]
        self.delStudent_icon = ctrl[4]
        self.OS = ctrl[5]
        self.main_path = ctrl[6]
        copyerr = ctrl[7]
        
        if copyerr: # if source dir is corrupt
            wx.MessageBox('Can not find the configuration file',
                          'Fatal Error', wx.ICON_STOP)
            print 'DrumsT: Fatal Error, can not find the source configuration'
            return False
        
        #---------------------Parsing file-conf-------------------------#
        conf = parser_fileconf() #parsing drumsT.conf
        self.school_db = 'schools.drtDB'
        self.path_db = conf
        
        if self.path_db == 'empty': # not set
            from drumsT_GUI.first_time_start import FirstStart
            main_frame = FirstStart(self.drumsT_icon)
            main_frame.Show()
            self.SetTopWindow(main_frame)
            return True
        
        elif self.path_db == 'error': # is corrupt
            wx.MessageBox('The configuration file is wrong',
                          'DrumsT: Fatal Error', wx.ICON_STOP)
            print 'drumsT: The configuration file is wrong'
            return False
        
        #--------------------Check paths--------------------------------#
        ret = control_db(self.path_db, self.school_db) #control existing 
        
        if not ret[0]:
            wx.MessageBox('The directory with database not exist !',
                          'DrumsT: Fatal Error', wx.ICON_STOP)
            print 'error: path db not exist'
            return False
        
        elif not ret[1]:
            wx.MessageBox('The database not exist in the path-name !',
                          'DrumsT: Fatal Error', wx.ICON_STOP)
            print 'error: file db not exist'
            return False
        
        else:
            from drumsT_GUI.mainwindow import MainFrame
            main_frame = MainFrame()
            main_frame.Show()
            self.SetTopWindow(main_frame)
            return True
    
if __name__ == "__main__":
    app = DrumsTeacher(False)
    app.MainLoop()
