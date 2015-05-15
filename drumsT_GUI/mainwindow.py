#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#
import wx
from drumsT_SYS.data_students import query, delete
import students_rec

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
        
        
        wx.Frame.__init__(self, None, -1, style=wx.DEFAULT_FRAME_STYLE)
        
        panel = wx.Panel(self)
        self.tool_bar()
        self.menu_bar()
        self.cmbx_school = wx.ComboBox(panel,wx.ID_ANY, choices=['not selected',
                                                                 'scuola1',
                                                                 'scuola2'],
                                       style=wx.CB_DROPDOWN | wx.CB_READONLY
                                       )
        self.cmbx_year = wx.ComboBox(panel,wx.ID_ANY, choices=['not selected',
                                                               '2015/2016',
                                                               '2016/2017',
                                                               '2017/2018',
                                                               '2018/2019'],
                                     style=wx.CB_DROPDOWN | wx.CB_READONLY
                                     )
        self.cmbx_level = wx.ComboBox(panel,wx.ID_ANY, choices=['not selected',
                                                                'basic',
                                                                'advanced',
                                                                'master'],
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
        self.cmbx_level.SetSelection(0)
        self.list_ctrl.SetBackgroundColour(green)
        self.list_ctrl.SetToolTipString("Select a profile to use")
        
        self.list_ctrl.InsertColumn(0, 'Name Surname', width=200)
        self.list_ctrl.InsertColumn(1, 'Address', width=300)
        self.list_ctrl.InsertColumn(2, 'Birth Date', width=150)
        self.list_ctrl.InsertColumn(3, 'Phone', width=180)
        self.list_ctrl.InsertColumn(4, 'Joined Date', width=150)
        self.list_ctrl.InsertColumn(5, 'Level-Course', width=400)
        
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
        
        
        self.reset_list()
        
    ################ COMMON METHODS FOR USEFUL
    def reset_list(self):
        """
        Delete all items of list_ctrl and pass to set_listctrl() for 
        re-charging new.
        """
        #self.list_ctrl.ClearAll() # 
        self.list_ctrl.DeleteAllItems()
        self.toolbar.EnableTool(wx.ID_FILE3, False)
        self.toolbar.EnableTool(wx.ID_FILE2, False)
        self.set_listctrl()
        
        
    def set_listctrl(self):
        """
        Populate the list_ctrl with data or new data. Before to use this
        method must be pass to reset_list() method first in the order:
        self.reset_list()
        self.set_listctrl()
        """
        profiles = query(self.path_db) # function for parsing
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
        self.toolbar.EnableTool(wx.ID_FILE3, True)
        self.toolbar.EnableTool(wx.ID_FILE2, True)
        
    def on_deselect(self, event): # list_ctrl
        """
        Event emitted when de-selecting all item
        """
        self.toolbar.EnableTool(wx.ID_FILE3, False)
        self.toolbar.EnableTool(wx.ID_FILE2, False)
        
    def on_enter(self, event): # list_ctrl
        """
        Type enter key or double clicked mouse event
        """
        print 'double click|enter'
    
    
    ######################################################################
    #------------------------Build the Tool Bar--------------------------#
    ######################################################################
    def tool_bar(self):
        """
        Makes and attaches the view tools bar
        """
        #--------- Properties
        self.toolbar = self.CreateToolBar(style=(wx.TB_HORZ_LAYOUT | wx.TB_TEXT))
        #self.toolbar.SetToolBitmapSize((32,32))
        self.toolbar.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        
        # ------- See student data
        pupil = self.toolbar.AddLabelTool(wx.ID_ANY, 'Open Selected Student', 
                                            wx.Bitmap(self.openStudent_ico))
        self.toolbar.AddSeparator()
        
        # ------- Add new student
        addpupil = self.toolbar.AddLabelTool(wx.ID_ANY, 'Add New Student', 
                                               wx.Bitmap(self.addStudent_ico))
        self.toolbar.AddSeparator()
        
        # ------- Modify student data
        modifypupil = self.toolbar.AddLabelTool(wx.ID_FILE2, 'data change student', 
                                             wx.Bitmap(self.changeStudent_ico))
        self.toolbar.AddSeparator()
        
        # ------- DSelete tudent
        deletepupil = self.toolbar.AddLabelTool(wx.ID_FILE3, 'data delete student', 
                                             wx.Bitmap(self.delStudent_ico))
        self.toolbar.AddSeparator()
        
        #---------------------Binding----------------------------#
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
        dialog = students_rec.AddRecords(self, 
                                     "Add new identity profile to database")
        ret = dialog.ShowModal()
        if ret == wx.ID_OK:
            self.reset_list() # clear and re-charging list_ctrl with newer
        
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

        
    #-----------------Callback menu bar (event handler)------------------#
    #------------------------------------------------------------------#
    def Addschool(self, event):
        print 'si'

        
        

#if __name__ == "__main__":
    
    #app = wx.App(False) #oppure: app = wx.App(0)
    #main_frame = MyFrame(None, wx.ID_ANY, "Sono il Frame")
    #app.SetTopWindow(main_frame)
    #main_frame.Show()
    #app.MainLoop()
 
