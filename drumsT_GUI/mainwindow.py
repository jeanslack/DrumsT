#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: mainwindow.py
# Porpose: main_frame
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (00) 15/05/2015
#########################################################
#
import wx
from drumsT_SYS import data_students
from drumsT_SYS import data_schools
from add_school import AddSchool
from drumsT_SYS.os_proc import create_rootdir
import students_rec
from drumsT_SYS.data_schools import Schools_Id
from drumsT_SYS.data_students import Students_Id

## COLORS:
azure = '#d9ffff' # rgb form (wx.Colour(217,255,255))
orange = '#ff5f1a' # rgb form (wx.Colour(255,95,26))
yellow = '#faff35'
red = '#ff3a1f'
green = '#deffb4'

class MainFrame(wx.Frame):

    def __init__(self):
        
        self.drumsT_ico = wx.GetApp().drumsT_icon
        self.addStudent_ico = wx.GetApp().addStudent_icon
        self.openStudent_ico = wx.GetApp().openStudent_icon
        self.delStudent_ico = wx.GetApp().delStudent_icon
        self.changeStudent_ico = wx.GetApp().changeStudent_icon
        self.path_db = wx.GetApp().path_db
        self.choice = None # schoolName/schoolYear
        
        self.students = data_students.Students_Id()
        school = ['not selected']
        self.school = data_schools.Schools_Id()
        call = self.school.query(self.path_db)
        #call = data_schools.query(self.path_db)
        for i in call:
            school.append(i[0])
            
        wx.Frame.__init__(self, None, -1, style=wx.DEFAULT_FRAME_STYLE)
        
        panel = wx.Panel(self)
        self.tool_bar()
        self.menu_bar()
        self.cmbx_school = wx.ComboBox(panel,wx.ID_ANY, choices=school,
                                       style=wx.CB_DROPDOWN | wx.CB_READONLY
                                       )
        self.cmbx_year = wx.ComboBox(panel,wx.ID_ANY, choices=['not selected'],
                                     style=wx.CB_DROPDOWN | wx.CB_READONLY
                                     )
        self.cmbx_level = wx.ComboBox(panel,wx.ID_ANY, choices=['not selected'],
                                      style=wx.CB_DROPDOWN | wx.CB_READONLY
                                      )
        self.list_ctrl = wx.ListCtrl(panel, wx.ID_ANY, style=wx.LC_REPORT | 
                                     wx.SUNKEN_BORDER
                                     )
        #################### Properties
        self.SetTitle(("Management School of Drums Course"))
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap(self.drumsT_ico, wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        self.SetSize((1100, 600))
        self.cmbx_school.SetSelection(0)
        self.cmbx_year.SetSelection(0)
        self.cmbx_year.Disable()
        self.cmbx_level.SetSelection(0)
        self.cmbx_level.Disable()
        self.list_ctrl.SetBackgroundColour(green)
        self.list_ctrl.SetToolTipString("Select a profile to use")
        
        self.list_ctrl.InsertColumn(0, 'Name Surname', width=200)
        self.list_ctrl.InsertColumn(1, 'Address', width=300)
        self.list_ctrl.InsertColumn(2, 'Birth Date', width=150)
        self.list_ctrl.InsertColumn(3, 'Phone', width=180)
        self.list_ctrl.InsertColumn(4, 'Joined Date', width=150)
        self.list_ctrl.InsertColumn(5, 'Level-Course', width=400)
        
        self.toolbar.EnableTool(wx.ID_FILE2, False)
        self.toolbar.EnableTool(wx.ID_FILE3, False)
        self.toolbar.EnableTool(wx.ID_FILE4, False)
        self.toolbar.EnableTool(wx.ID_FILE5, False)
        
        ####################  Set layout
        siz_base = wx.FlexGridSizer(2,1,0,0)
        grd_s1 = wx.FlexGridSizer(1,3,0,40)
        #box_school.Lower()
        box_school = wx.StaticBox(panel, wx.ID_ANY, "Select a school location:")
        school = wx.StaticBoxSizer(box_school, wx.VERTICAL)
        school.Add(self.cmbx_school, wx.EXPAND,0)
        
        box_year = wx.StaticBox(panel, wx.ID_ANY, "Select a school year:")
        year = wx.StaticBoxSizer(box_year, wx.VERTICAL)
        year.Add(self.cmbx_year, wx.EXPAND,0)
        
        box_level = wx.StaticBox(panel, wx.ID_ANY, "Select a course level:")
        level = wx.StaticBoxSizer(box_level, wx.VERTICAL)
        level.Add(self.cmbx_level, wx.EXPAND,0)
        
        grd_s1.AddMany([(school),(year),(level)])
        
        siz_base.Add(grd_s1, 0, wx.ALL, 15)
        siz_base.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 15)
        
        panel.SetSizer(siz_base)
        siz_base.AddGrowableCol(0)
        siz_base.AddGrowableRow(1)
        siz_base.AddGrowableCol(1)
        #self.Layout()
        self.Centre()
        
        ######################## binding #####################
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_select, self.list_ctrl)
        self.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.on_deselect, self.list_ctrl)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.on_enter, self.list_ctrl)
        self.cmbx_school.Bind(wx.EVT_COMBOBOX, self.on_school)
        self.cmbx_year.Bind(wx.EVT_COMBOBOX, self.on_year)
        self.cmbx_school.Bind(wx.EVT_TEXT, self.on_change_school)

    ################ COMMON METHODS USEFUL
    def set_listctrl(self):
        """
        Populate the list_ctrl with data or new data. Before to use this
        method first must be use self.list_ctrl.DeleteAllItems() otherwise 
        append result in the list_ctrl
        """
        #print self.choice
        path = '%s/%s/students.drtDB' % (self.path_db, self.choice)
        profiles = self.students.query(path)
        
        if profiles == []:
            wx.MessageBox("There isn't any list to load.\n"
                          "You must add new students now", 
                          'Empty database', wx.ICON_EXCLAMATION, self)
            return
        index = 0
        for rec in profiles:
            rows = self.list_ctrl.InsertStringItem(index, rec[0])
            self.list_ctrl.SetStringItem(rows, 0, rec[0])
            self.list_ctrl.SetStringItem(rows, 1, rec[1])
            self.list_ctrl.SetStringItem(rows, 2, rec[2])
            self.list_ctrl.SetStringItem(rows, 3, rec[3])
            self.list_ctrl.SetStringItem(rows, 4, rec[4])
            self.list_ctrl.SetStringItem(rows, 5, rec[5])
        
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
    def on_school(self, event): # combobox
        """
        When select a item in combobox school go in.
        """
        if self.cmbx_school.GetValue() == 'not selected':
            self.cmbx_year.Clear()
            self.cmbx_year.Append('not selected')
            self.cmbx_year.SetSelection(0)
            self.cmbx_year.Disable()
        else:
            key = self.cmbx_school.GetValue()
            self.cmbx_year.Enable()
            self.cmbx_year.Clear()
            #self.cmbx_year.SetValue(' ')
            self.cmbx_year.Append('not selected')
            year = self.school.key_query(self.path_db, key)
            for items in year:
                self.cmbx_year.Append(items[0])
            self.cmbx_year.SetSelection(0)
    #-------------------------------------------------------------------#
    def on_year(self, event): # combobox
        """
        When select a item in combobox year go in
        """
        if self.cmbx_year.GetValue() == 'not selected':
            self.list_ctrl.DeleteAllItems()
            self.toolbar.EnableTool(wx.ID_FILE2, False)
            self.toolbar.EnableTool(wx.ID_FILE3, False)
            self.toolbar.EnableTool(wx.ID_FILE4, False)
            self.toolbar.EnableTool(wx.ID_FILE5, False)
        else:
            school = self.cmbx_school.GetValue()
            year = self.cmbx_year.GetValue()
            self.choice = '%s/%s' % (school,year)
            self.toolbar.EnableTool(wx.ID_FILE3, True)
            self.list_ctrl.DeleteAllItems()
            self.set_listctrl()
    #-------------------------------------------------------------------#
    def on_change_school(self, event): # combobox
        """
        when you change school selection in combobox resets to default 
        """
        self.list_ctrl.DeleteAllItems()
        self.toolbar.EnableTool(wx.ID_FILE2, False)
        self.toolbar.EnableTool(wx.ID_FILE3, False)
        self.toolbar.EnableTool(wx.ID_FILE4, False)
        self.toolbar.EnableTool(wx.ID_FILE5, False)

    ######################################################################
    #------------------------Build the Tool Bar--------------------------#
    ######################################################################
    def tool_bar(self):
        """
        Makes and attaches the view tools bar
        """
        #--------- Properties
        self.toolbar = self.CreateToolBar(style=(wx.TB_HORZ_LAYOUT | wx.TB_TEXT))
        self.toolbar.SetToolBitmapSize((32,32))
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
        Add one new record to database
        """
        path = '%s/%s' % (self.path_db,self.choice)
        dialog = students_rec.AddRecords(self, 
                                  "Add new identity profile to database", path)
        ret = dialog.ShowModal()
        if ret == wx.ID_OK:
            self.list_ctrl.DeleteAllItems() # clear all items in list_ctrl
            self.set_listctrl() # re-charging list_ctrl with newer
        
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

        dialog = AddSchool(self, "DrumsT - Add new school and date")
        retcode = dialog.ShowModal()

        if retcode == wx.ID_OK:
            data = dialog.GetValue()
        else:
            return

        mkdirs = create_rootdir(self.path_db,data[0],data[1])
        if mkdirs[0]:
            wx.MessageBox(mkdirs[1], 'ERROR', wx.ICON_ERROR, self)
            return
        schools = Schools_Id().new_school(self.path_db,data[0],data[1])
        #if schools[0]:
            #wx.MessageBox(schools[1], 'ERROR', wx.ICON_ERROR, self)
            #return
        students = Students_Id().first_start(self.path_db,data[0],data[1])
        if students[0]:
            wx.MessageBox(students[1], 'ERROR', wx.ICON_ERROR, self)
            return
    #------------------------------------------------------------------#
    def Addate(self, event):
        date = '2013_2014'
        
        

        
        

#if __name__ == "__main__":
    
    #app = wx.App(False) #oppure: app = wx.App(0)
    #main_frame = MyFrame(None, wx.ID_ANY, "Sono il Frame")
    #app.SetTopWindow(main_frame)
    #main_frame.Show()
    #app.MainLoop()
 
