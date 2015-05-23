#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: mainwindow.py
# Porpose: main_frame
# Author: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (00) 15/05/2015
#########################################################
#
import wx
#import os
import add_student, add_school, add_newyear
from drumsT_SYS.os_filesystem import create_rootdir
from drumsT_SYS.SQLite_lib import School_Class

## COLORS:
azure = '#d9ffff' # rgb form (wx.Colour(217,255,255))
orange = '#ff5f1a' # rgb form (wx.Colour(255,95,26))
yellow = '#faff35'
red = '#ff3a1f'
green = '#deffb4'
greendeph = '#91ff8f'

class MainFrame(wx.Frame):

    def __init__(self):
        
        self.drumsT_ico = wx.GetApp().drumsT_icon
        self.addStudent_ico = wx.GetApp().addStudent_icon
        self.openStudent_ico = wx.GetApp().openStudent_icon
        self.delStudent_ico = wx.GetApp().delStudent_icon
        self.changeStudent_ico = wx.GetApp().changeStudent_icon
        # base diractory to save any db:
        self.rootdir = wx.GetApp().rootdir
        self.IDyear = None # int db school
        # name of school:
        self.schoolName = None
        # path name of current file .drtDB :
        self.path_db = None
        
        self.school = School_Class()
        
        wx.Frame.__init__(self, None, -1, style=wx.DEFAULT_FRAME_STYLE)
        panel = wx.Panel(self)
        self.tool_bar()
        self.menu_bar()
        self.sb = self.CreateStatusBar(0)
        import_btn = wx.Button(panel, wx.ID_ANY, ("Import"))
        self.cmbx_year = wx.ComboBox(panel,wx.ID_ANY, choices=['not selected'],
                                     style=wx.CB_DROPDOWN | wx.CB_READONLY
                                     )
        self.import_txt = wx.TextCtrl(panel, wx.ID_ANY, "", style=wx.TE_READONLY)
        self.list_ctrl = wx.ListCtrl(panel, wx.ID_ANY, style=wx.LC_REPORT | 
                                     wx.SUNKEN_BORDER
                                     )
        #################### Properties
        self.SetTitle(("Management School of Drums Course"))
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap(self.drumsT_ico, wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        self.SetSize((1100, 600))
        import_btn.SetMinSize((180, 20))
        import_btn.SetBackgroundColour(azure)
        self.cmbx_year.SetSelection(0)
        self.cmbx_year.Disable()
        self.import_txt.SetMinSize((270, 20))
        self.import_txt.Disable()
        #self.list_ctrl.SetBackgroundColour(green)
        self.list_ctrl.SetToolTipString("Double click to open a individual profile")
        
        self.list_ctrl.InsertColumn(0, 'School Year', width=100)
        self.list_ctrl.InsertColumn(1, 'Name', width=120)
        self.list_ctrl.InsertColumn(2, 'Surname', width=120)
        self.list_ctrl.InsertColumn(3, 'Phone', width=180)
        self.list_ctrl.InsertColumn(4, 'Address', width=300)
        self.list_ctrl.InsertColumn(5, 'Birth Date', width=150)
        self.list_ctrl.InsertColumn(6, 'Joined Date', width=150)
        self.list_ctrl.InsertColumn(7, 'Level-Course', width=400)
        
        self.toolbar.EnableTool(wx.ID_FILE2, False)
        self.toolbar.EnableTool(wx.ID_FILE3, False)
        self.toolbar.EnableTool(wx.ID_FILE4, False)
        self.toolbar.EnableTool(wx.ID_FILE5, False)
        
        ####################  Set layout
        siz_base = wx.FlexGridSizer(2,1,0,0)
        grd_s1 = wx.FlexGridSizer(1,3,0,40)
        #box_school.Lower()
        box_school = wx.StaticBox(panel, wx.ID_ANY, "School Database Importing:")
        school = wx.StaticBoxSizer(box_school, wx.VERTICAL)
        school.Add(import_btn, wx.EXPAND,0)
        
        box_txt = wx.StaticBox(panel, wx.ID_ANY, "Name Database Imported:")
        dbname = wx.StaticBoxSizer(box_txt, wx.VERTICAL)
        dbname.Add(self.import_txt, wx.EXPAND,0)
        
        box_year = wx.StaticBox(panel, wx.ID_ANY, "School Year selection:")
        year = wx.StaticBoxSizer(box_year, wx.VERTICAL)
        year.Add(self.cmbx_year, wx.EXPAND,0)

        grd_s1.AddMany([(school),(dbname),(year)])
        
        siz_base.Add(grd_s1, 0, wx.ALL, 15)
        siz_base.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 15)
        
        panel.SetSizer(siz_base)
        siz_base.AddGrowableCol(0)
        siz_base.AddGrowableRow(1)
        siz_base.AddGrowableCol(1)
        self.Layout()
        self.Centre()
        ######################## binding #####################
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_select, self.list_ctrl)
        self.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.on_deselect, self.list_ctrl)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.on_enter, self.list_ctrl)
        self.Bind(wx.EVT_BUTTON, self.open_school, import_btn)
        self.cmbx_year.Bind(wx.EVT_COMBOBOX, self.on_year)
        
    ################ COMMON METHODS USEFUL
    def statusbar_msg(self, msg, color):
        """
        set the status-bar with messages and color types
        """
        if color == None:
            self.sb.SetBackgroundColour(wx.NullColour)
        else:
            self.sb.SetBackgroundColour(color)
            
        self.sb.SetStatusText(msg)
        self.sb.Refresh()
    ################ COMMON METHODS USEFUL
    def set_listctrl(self):
        """
        Populate the list_ctrl with data or new data. Before to use this
        method first must be use self.list_ctrl.DeleteAllItems() otherwise 
        append result in the list_ctrl
        """
        profiles = self.school.displayclass(self.path_db, self.IDyear)
        if profiles == []:
            msg = ("Info - Empty database: There isn't any list to load. "
                "You must add new students now")
            self.statusbar_msg(msg, greendeph)
            return

        index = 0
        for rec in profiles:
            rows = self.list_ctrl.InsertStringItem(index, rec[1])
            self.list_ctrl.SetStringItem(rows, 0, rec[1])
            self.list_ctrl.SetStringItem(rows, 1, rec[2])
            self.list_ctrl.SetStringItem(rows, 2, rec[3])
            self.list_ctrl.SetStringItem(rows, 3, rec[4])
            self.list_ctrl.SetStringItem(rows, 4, rec[5])
            self.list_ctrl.SetStringItem(rows, 5, rec[6])
            self.list_ctrl.SetStringItem(rows, 6, rec[7])
            self.list_ctrl.SetStringItem(rows, 7, rec[8])
            
    #-----------------------EVENTS--------------------------------------#
    def on_select(self, event): # list_ctrl
        """
        Event emitted when selecting item only
        """
        slct = event.GetText() # event.GetText is a Name Profile
        self.toolbar.EnableTool(wx.ID_FILE2, True)
        self.toolbar.EnableTool(wx.ID_FILE4, True)
        self.toolbar.EnableTool(wx.ID_FILE5, True)
    #-------------------------------------------------------------------#
    def on_deselect(self, event): # list_ctrl
        """
        Event emitted when de-selecting all item
        """
        self.toolbar.EnableTool(wx.ID_FILE2, False)
        self.toolbar.EnableTool(wx.ID_FILE4, False)
        self.toolbar.EnableTool(wx.ID_FILE5, False)
    #-------------------------------------------------------------------#
    def on_enter(self, event): # list_ctrl
        """
        Type enter key or double clicked mouse event
        """
        print 'double click|enter'
    #-------------------------------------------------------------------#
    def open_school(self, event): # import button
        """
        Open a existing database with .drtDB extension. The filedialog 
        is set to opening in the 'drumsT_DB' directory 
        """
        wildcard = ("drumsT db (*.drtDB)|*.drtDB|" "All files (*.*)|*.*")
        dialfile = wx.FileDialog(self, 
                       "Select filename with '.drtDB' extension ",
                       ".", "", wildcard, wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        dialfile.SetDirectory(self.rootdir)
        
        if dialfile.ShowModal() == wx.ID_OK: 
            self.schoolName = dialfile.GetFilename().split(".drtDB")[0]
            self.path_db = dialfile.GetPath()
            self.cmbx_year.Enable(), self.cmbx_year.Clear()
            self.cmbx_year.Append('not selected')
            year = self.school.displayschool(self.path_db)

            for items in year:
                self.cmbx_year.Append(items[0])# can be more data
                
            self.cmbx_year.SetSelection(0)
            self.import_txt.Enable(), self.import_txt.SetValue("")
            self.import_txt.AppendText(dialfile.GetFilename())
            
            if self.list_ctrl.GetItemCount() > 0:# if list_ctrl is not empty
                self.list_ctrl.DeleteAllItems()
                self.toolbar.EnableTool(wx.ID_FILE2, False)
                self.toolbar.EnableTool(wx.ID_FILE3, False)
                self.toolbar.EnableTool(wx.ID_FILE4, False)
                self.toolbar.EnableTool(wx.ID_FILE5, False)
    #-------------------------------------------------------------------#
    def on_year(self, event): # combobox
        """
        When select a item in cmbx_year go in this setup
        """
        if self.cmbx_year.GetValue() == 'not selected':
            self.list_ctrl.DeleteAllItems()
            self.toolbar.EnableTool(wx.ID_FILE2, False)
            self.toolbar.EnableTool(wx.ID_FILE3, False)
            self.toolbar.EnableTool(wx.ID_FILE4, False)
            self.toolbar.EnableTool(wx.ID_FILE5, False)
        else:
            #year = self.cmbx_year.GetValue()
            self.IDyear = self.cmbx_year.GetValue()
            self.toolbar.EnableTool(wx.ID_FILE3, True)
            self.list_ctrl.DeleteAllItems()
            self.set_listctrl()
    #-------------------------------------------------------------------#

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
        pupil = self.toolbar.AddLabelTool(wx.ID_FILE2, 'Open Selected Student',
                                          wx.Bitmap(self.openStudent_ico))
        self.toolbar.AddSeparator()
        
        # ------- Add new student
        addpupil = self.toolbar.AddLabelTool(wx.ID_FILE3, 'Add New Student', 
                                               wx.Bitmap(self.addStudent_ico))
        self.toolbar.AddSeparator()
        
        # ------- Modify student data
        modifypupil = self.toolbar.AddLabelTool(wx.ID_FILE4, 'data change student', 
                                             wx.Bitmap(self.changeStudent_ico))
        self.toolbar.AddSeparator()
        
        # ------- DSelete tudent
        deletepupil = self.toolbar.AddLabelTool(wx.ID_FILE5, 'data delete student', 
                                             wx.Bitmap(self.delStudent_ico))
        self.toolbar.AddSeparator()
        
        # ----------- finally, create it
        self.toolbar.Realize()
        
        #------------ Binding
        self.Bind(wx.EVT_TOOL, self.Pupil, pupil)
        self.Bind(wx.EVT_TOOL, self.Addpupil, addpupil)
        self.Bind(wx.EVT_TOOL, self.Modify, modifypupil)
        self.Bind(wx.EVT_TOOL, self.Delete, deletepupil)
        
    #-------------------------EVENTS-----------------------------------#
    #------------------------------------------------------------------#

    def Pupil(self, event):
        print 'apri scheda alunno'
        
    #------------------------------------------------------------------#
    def Addpupil(self, event):
        """
        Add one new record to Class table
        """
        dialog = add_student.AddRecords(self, 
                                      "Add new identity profile to database", 
                                       self.path_db,self.IDyear)
        ret = dialog.ShowModal()
        if ret == wx.ID_OK:
            self.list_ctrl.DeleteAllItems() # clear all items in list_ctrl
            self.set_listctrl() # re-charging list_ctrl with newer
            
        if schools[0]:
            wx.MessageBox(schools[1], 'ERROR', wx.ICON_ERROR, self)
            return
            
        self.statusbar_msg('', None)
    #------------------------------------------------------------------#
    def Modify(self, event):
        print 'modifica alunno'
        
    #------------------------------------------------------------------#
    def Delete(self, event):
        print 'cancella alunno'


    ######################################################################
    #------------------------Build Menu Bar-----------------------------#
    ######################################################################
    def menu_bar(self):
        """
        Makes and attaches the view menu

        """
        menuBar = wx.MenuBar()

        #------------------- Strumenti
        schoolButton = wx.Menu()
        
        addschool = schoolButton.Append(wx.ID_ANY, "Add new school", 
                                            "Create a new record for school")
        addate = schoolButton.Append(wx.ID_ANY, "Add new year to selected school", 
                                           "Create a new record for school")
        modifyschool = schoolButton.Append(wx.ID_ANY, "Modify school name", 
                                     "Create a new record for school")
        deleteschool = schoolButton.Append(wx.ID_ANY, "Delete a school", 
                                     "Create a new record for school")
        
        menuBar.Append(schoolButton,"Schools")
        
        pupilsButton = wx.Menu()
        addpupil = pupilsButton.Append(wx.ID_ANY, "Add new pupil", 
                                       "Create a new record for school")
        addmorepupil = pupilsButton.Append(wx.ID_ANY, "Add more one new pupil", 
                                      "Create a new record for school")
        modifypupil = pupilsButton.Append(wx.ID_ANY, "Modify data pupil", 
                                       "Create a new record for school")
        deletepupil = pupilsButton.Append(wx.ID_ANY, "Delete a pupil", 
                                          "Create a new record for school")
        
        menuBar.Append(pupilsButton,"Alumns")
        
        # ...and set, finally .
        self.SetMenuBar(menuBar)


        #-----------------------Binding menu bar-------------------------#
        # menu tools
        self.Bind(wx.EVT_MENU, self.Addschool, addschool)
        self.Bind(wx.EVT_MENU, self.Addate, addate)

        
    #-----------------Callback menu bar (event handler)------------------#
    #------------------------------------------------------------------#
    def Addschool(self, event):
        """
        Add new school database to school directory
        """

        dialog = add_school.AddSchool(self, "DrumsT - Add new school and date")
        retcode = dialog.ShowModal()

        if retcode == wx.ID_OK:
            data = dialog.GetValue()
        else:
            return
        
        mkdirs = create_rootdir(self.rootdir,data[0])
        if mkdirs[0]:
            wx.MessageBox(mkdirs[1], 'ERROR', wx.ICON_ERROR, self)
            return
        schools = School_Class().newSchoolyear(self.rootdir,data[0],data[1])
        if schools[0]:
            wx.MessageBox(schools[1], 'ERROR', wx.ICON_ERROR, self)
            return
        
        wx.MessageBox('DrumsT: Success on create new school', 'ERROR', 
                      wx.ICON_ERROR, self)
    #------------------------------------------------------------------#
    def Addate(self, event):
        """
        Add new date event
        """
        dialog = add_newyear.AddYear(self, "DrumsT")
        retcode = dialog.ShowModal()
        
        if retcode == wx.ID_OK:
            data = dialog.GetValue()
        else:
            return
        
        schools = School_Class().add_date(self.path_db,data)
        self.cmbx_year.Append(data)
        
        

        
        

#if __name__ == "__main__":
    
    #app = wx.App(False) #oppure: app = wx.App(0)
    #main_frame = MyFrame(None, wx.ID_ANY, "Sono il Frame")
    #app.SetTopWindow(main_frame)
    #main_frame.Show()
    #app.MainLoop()
 
