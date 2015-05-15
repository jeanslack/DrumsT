#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import wx
from drumsT_SYS.boot import control_config, parser_fileconf

class DrumsTeacher(wx.App):
    """
    This is a bootstrap interface
    """
    def OnInit(self):
        """
        Main initilize ctrl
        """
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
        
        conf = parser_fileconf() #parsing drumsT.conf
        self.path_db = conf
        
        if self.path_db == 'empty':
            from drumsT_GUI.first_time_start import MyDialog
            main_frame = MyDialog(self.drumsT_icon)
            main_frame.Show()
            self.SetTopWindow(main_frame)
            return True
        
        elif self.path_db == 'error':
            wx.MessageBox('The configuration file is wrong',
                          'Fatal Error', wx.ICON_STOP)
            print 'drumsT: The configuration file is wrong'
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
