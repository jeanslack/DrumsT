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
import add_student, add_school, add_newyear, lessons
from drumsT_SYS.os_filesystem import create_rootdir
from drumsT_SYS.SQLite_lib import School_Class

## COLORS:
azure = '#d9ffff' # rgb form (wx.Colour(217,255,255))
orange = '#ff5f1a' # rgb form (wx.Colour(255,95,26))
yellow = '#faff35'
red = '#ff3a1f'
greenolive = '#deffb4'
greenlight = '#91ff8f'
greendeph = '#516c1a'

class MainFrame(wx.Frame):
    """
    This is a main window of the selections and the 
    databases importing. 
    """
    def __init__(self):
        """
        Here set the attributes that pass at others dialogs and frame
        """
        #################### set attributes:
        self.drumsT_ico = wx.GetApp().drumsT_icon
        self.addStudent_ico = wx.GetApp().addStudent_icon
        self.openStudent_ico = wx.GetApp().openStudent_icon
        self.delStudent_ico = wx.GetApp().delStudent_icon
        self.changeStudent_ico = wx.GetApp().changeStudent_icon
        ####
        self.rootdir = wx.GetApp().rootdir # base diractory to save any db
        self.path_db = None # path name of current file .drtDB
        self.IDyear = None # db school year id
        self.schoolName = None # name of school
        self.IDprofile = None # identifier (IDclass integear) 
        self.name = None # name of a student
        self.surname = None # surname of a student
        self.phone = None
        self.address = None
        self.birthDate = None
        self.joinDate = None
        self.level = None
        
        ####################
        wx.Frame.__init__(self, None, -1, style=wx.DEFAULT_FRAME_STYLE)
        
        self.InitUI()
        
    def InitUI(self):
        """
        start with widgets and setup
        """
        panel = wx.Panel(self, wx.ID_ANY)
        self.tool_bar()
        self.menu_bar()
        self.sb = self.CreateStatusBar(0)
        import_btn = wx.Button(panel, wx.ID_ANY, ("Import"))
        self.cmbx_year = wx.ComboBox(panel,wx.ID_ANY, choices=['not selected'],
                                     style=wx.CB_DROPDOWN | wx.CB_READONLY
                                     )
        self.import_txt = wx.TextCtrl(panel, wx.ID_ANY, "", 
                                      style=wx.TE_READONLY | wx.TE_CENTRE
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
        import_btn.SetMinSize((180, 20))
        import_btn.SetBackgroundColour(greenlight)
        self.cmbx_year.SetSelection(0)
        self.cmbx_year.Disable()
        self.import_txt.SetMinSize((270, 20))
        self.import_txt.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.import_txt.SetForegroundColour(greendeph)
        self.import_txt.Disable()
        self.list_ctrl.SetToolTipString("Double click to open a individual profile")
        
        self.list_ctrl.InsertColumn(0, 'ID', width=30)
        self.list_ctrl.InsertColumn(1, 'School Year', width=100)
        self.list_ctrl.InsertColumn(2, 'Name', width=120)
        self.list_ctrl.InsertColumn(3, 'Surname', width=120)
        self.list_ctrl.InsertColumn(4, 'Phone', width=140)
        self.list_ctrl.InsertColumn(5, 'Address', width=300)
        self.list_ctrl.InsertColumn(6, 'Birth Date', width=150)
        self.list_ctrl.InsertColumn(7, 'Joined Date', width=150)
        self.list_ctrl.InsertColumn(8, 'Level-Course', width=400)
        
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
        siz_base.Fit(panel) 
        siz_base.AddGrowableCol(0)
        siz_base.AddGrowableRow(1)
        self.Layout()
        self.Centre()
        ######################## binding #####################
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_select, self.list_ctrl)
        self.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.on_deselect, self.list_ctrl)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.on_enter, self.list_ctrl)
        self.Bind(wx.EVT_BUTTON, self.open_school, import_btn)
        self.cmbx_year.Bind(wx.EVT_COMBOBOX, self.on_year)
        
    #-------------------------------------------------------#
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
    #-------------------------------------------------------#
    def set_listctrl(self):
        """
        Populate the list_ctrl with data or new data. Before to use this
        method first must be use self.list_ctrl.DeleteAllItems() method 
        otherwise append result upon in the list_ctrl
        """
        profiles = School_Class().displayclass(self.path_db, self.IDyear)
        if profiles == []:
            msg = ("Info - Empty database: There isn't any list to load. "
                "You must add new students now")
            self.statusbar_msg(msg, yellow)
            self.toolbar.EnableTool(wx.ID_FILE2, False)
            self.toolbar.EnableTool(wx.ID_FILE4, False)
            self.toolbar.EnableTool(wx.ID_FILE5, False)
            return

        index = 0
        for rec in profiles:
            rows = self.list_ctrl.InsertStringItem(index, str(rec[0]))
            self.list_ctrl.SetStringItem(rows, 0, str(rec[0]))
            self.list_ctrl.SetStringItem(rows, 1, rec[1])
            self.list_ctrl.SetStringItem(rows, 2, rec[2])
            self.list_ctrl.SetStringItem(rows, 3, rec[3])
            self.list_ctrl.SetStringItem(rows, 4, rec[4])
            self.list_ctrl.SetStringItem(rows, 5, rec[5])
            self.list_ctrl.SetStringItem(rows, 6, rec[6])
            self.list_ctrl.SetStringItem(rows, 7, rec[7])
            self.list_ctrl.SetStringItem(rows, 8, rec[8])
            if index % 2:
                self.list_ctrl.SetItemBackgroundColour(index, "white")
            else:
                 self.list_ctrl.SetItemBackgroundColour(index, greenolive)
            index += 1
            
    ########################### START WITH EVENTS HANDLER
    #------------------------------------------------------------------#
    def on_select(self, event): # list_ctrl
        """
        Event emitted when selecting item only.
        """
        index = self.list_ctrl.GetFocusedItem()
        item_ID = self.list_ctrl.GetItem(index,0)
        item_name = self.list_ctrl.GetItem(index,2)
        item_surname = self.list_ctrl.GetItem(index,3)
        item_phone = self.list_ctrl.GetItem(index,4)
        item_addr = self.list_ctrl.GetItem(index,5)
        item_birth = self.list_ctrl.GetItem(index,6)
        item_join = self.list_ctrl.GetItem(index,7)
        item_lev = self.list_ctrl.GetItem(index,8)
        
        self.IDprofile = item_ID.GetText()
        self.name = "%s" % (item_name.GetText())
        self.surname = "%s" % (item_surname.GetText())
        self.phone = "%s" % (item_phone.GetText())
        self.address = "%s" % (item_addr.GetText())
        self.birthDate = "%s" % (item_birth.GetText())
        self.joinDate = "%s" % (item_join.GetText())
        self.level = "%s" % (item_lev.GetText())
        
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
        self.IDprofile = None
    #-------------------------------------------------------------------#
    def on_enter(self, event): # list_ctrl
        """
        If type enter key or double clicked mouse, the event 
        open a Lesson
        """
        nameSur = "%s %s" % (self.name,self.surname)
        frame = lessons.Lesson(nameSur, self.IDprofile, self.path_db)
        frame.Show()
        #schools = School_Class().displaystudent(self.IDprofile ,self.path_db)
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
            year = School_Class().displayschool(self.path_db)

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
            self.statusbar_msg('', None)
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
        pupil = self.toolbar.AddLabelTool(wx.ID_FILE2, 'Open lesson in selection',
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
        """
        open a Lesson
        """
        self.on_enter(self)
    #------------------------------------------------------------------#
    def Addpupil(self, event):
        """
        Add one new record to Class table
        """
        dialog = add_student.AddRecords(self,
                                        "Add new identity profile to database",
                                        None,None,None,None,None,None, None
                                        )
        ret = dialog.ShowModal()
        
        if ret == wx.ID_OK:
            data = dialog.GetValue()
            check = School_Class().checkstudent(data[0],data[1],
                                                self.path_db, self.IDyear)
        else:
            return
            
        if check[0]:
            warn = wx.MessageDialog(self, check[1], "Warning", wx.YES_NO | 
                                    wx.CANCEL | wx.ICON_EXCLAMATION)
            
            if warn.ShowModal() == wx.ID_YES:
                pass
            else:
                return
            
        add = School_Class().insertstudent(data[0],data[1],data[2],data[3],
                          data[4],data[5],data[6],self.path_db, self.IDyear)
        wx.MessageBox("Successfull storing !", "Success", wx.OK, self)

        self.list_ctrl.DeleteAllItems() # clear all items in list_ctrl
        self.set_listctrl() # re-charging list_ctrl with newer
        self.statusbar_msg('', None)
    #------------------------------------------------------------------#
    def Modify(self, event):
        """
        change data identity of the selected item
        """
        
        dialog = add_student.AddRecords(self,
                                 "Change data into selected identity profile",
                                 self.name,self.surname, self.phone, 
                                 self.address,self.birthDate,self.joinDate,
                                 self.level
                                        )
        ret = dialog.ShowModal()
        if ret == wx.ID_OK:
            data = dialog.GetValue()
            check = School_Class().checkstudent(data[0],data[1],
                                                self.path_db, self.IDyear)
        else:
            return
            
        if check[0]:
            warn = wx.MessageDialog(self, check[1], "Warning", wx.YES_NO | 
                                    wx.CANCEL | wx.ICON_EXCLAMATION)
            
            if warn.ShowModal() == wx.ID_YES:
                pass
            else:
                return
            
        change = School_Class().change_class_item(data[0],data[1],data[2],
                                                  data[3],data[4],data[5],
                                                  data[6], self.IDprofile,
                                                  self.path_db
                                                  )
        wx.MessageBox("Successfull storing !", "Success", wx.OK, self)

        self.list_ctrl.DeleteAllItems() # clear all items in list_ctrl
        self.set_listctrl() # re-charging list_ctrl with newer
        self.statusbar_msg('Update new profile', None)
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
        addlesson = pupilsButton.Append(wx.ID_ANY, "Add new pupil", 
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
        self.Bind(wx.EVT_MENU, self.Addlesson, addlesson)

        
    #-----------------Callback menu bar (event handler)------------------#
    #------------------------------------------------------------------#
    def Addschool(self, event):
        """
        Add new school with a school year. This method make a new directory
        with school name and insert data to database.
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
        
        wx.MessageBox('DrumsT: Success on create new school', 'Info',
                      wx.ICON_INFORMATION, self)
    #------------------------------------------------------------------#
    def Addate(self, event):
        """
        Add new date event into selected school.
        """
        dialog = add_newyear.AddYear(self, "DrumsT")
        retcode = dialog.ShowModal()
        
        if retcode == wx.ID_OK:
            data = dialog.GetValue()
        else:
            return
        
        schools = School_Class().updateyear(self.path_db, data)
        if schools:
            wx.MessageBox("DrumsT: This school year already exist, is not "
                          "possible add this record", 'WARNING', 
                          wx.ICON_EXCLAMATION, self)
            return
        wx.MessageBox('DrumsT: Success on create new year', 'Info', 
                      wx.ICON_INFORMATION, self)
        self.cmbx_year.Append(data)
        
        
    def Addlesson(self, event):
        frame = lesson.InsertLesson(self)
        frame.Show()
