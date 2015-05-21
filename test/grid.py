#import wx
#import wx.grid

#class GridFrame(wx.Frame):

    #def __init__(self, parent):

        #wx.Frame.__init__(self, parent)

        ## Create a wxGrid object
        #grid = wx.grid.Grid(self, -1)

        ## Then we call CreateGrid to set the dimensions of the grid
        ## (100 rows and 10 columns in this example)
        #grid.CreateGrid(100, 10)

        ## We can set the sizes of individual rows and columns
        ## in pixels
        #grid.SetRowSize(0, 60)
        #grid.SetColSize(0, 120)

        ## And set grid cell contents as strings
        #grid.SetCellValue(0, 0, 'wxGrid is good')

        ## We can specify that some cells are read.only
        #grid.SetCellValue(0, 3, 'This is read.only')
        #grid.SetReadOnly(0, 3)

        ## Colours can be specified for grid cell contents
        #grid.SetCellValue(3, 3, 'green on grey')
        #grid.SetCellTextColour(3, 3, wx.GREEN)
        #grid.SetCellBackgroundColour(3, 3, wx.LIGHT_GREY)

        ## We can specify the some cells will store numeric
        ## values rather than strings. Here we set grid column 5
        ## to hold floating point values displayed with width of 6
        ## and precision of 2
        #grid.SetColFormatFloat(5, 6, 2)
        #grid.SetCellValue(0, 6, '3.1415')

        #self.Show()


#if __name__ == '__main__':

    #app = wx.App(0)
    #frame = GridFrame(None)
    #app.MainLoop() 
    
import wx
import wx.grid as  gridlib
 
class MyForm(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "Grid with Popup Menu")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        self.grid = gridlib.Grid(panel)
        self.grid.CreateGrid(25,8)
        self.grid.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK,
                       self.showPopupMenu)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND, 5)
        panel.SetSizer(sizer)
 
    #----------------------------------------------------------------------
    def showPopupMenu(self, event):
        """
        Create and display a popup menu on right-click event
        """
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popupID2 = wx.NewId()
            self.popupID3 = wx.NewId()
            # make a menu
 
        menu = wx.Menu()
        # Show how to put an icon in the menu
        item = wx.MenuItem(menu, self.popupID1,"One")
        menu.AppendItem(item)
        menu.Append(self.popupID2, "Two")
        menu.Append(self.popupID3, "Three")
 
        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()
 
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()
