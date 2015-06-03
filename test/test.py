#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx 
import wx.grid 

class MyGrid(wx.grid.Grid): 

    def __init__(self, parent = None, style = wx.WANTS_CHARS): 

        wx.grid.Grid.__init__(self, parent, -1, style = style) 

        self.CreateGrid(10, 10) 

        self.editor = wx.grid.GridCellAutoWrapStringEditor() 
        self.SetDefaultEditor(self.editor)

        self.SetDefaultRenderer(wx.grid.GridCellAutoWrapStringRenderer()) 

        self.SetCellValue(0, 0, "Line1\nLine2\nLine3") 
        self.SetRowSize(0, 100) 


class MyFrame(wx.Frame): 

    def __init__(self, parent = None, title = "Multiline"): 

        wx.Frame.__init__(self, parent, -1, title) 

        self.Bind(wx.EVT_CHAR_HOOK, self.on_frame_char_hook) 

        panel = wx.Panel(self) 

        vbox = wx.BoxSizer(wx.VERTICAL) 
        panel.SetSizer(vbox) 

        grid = MyGrid(panel) 
        vbox.Add(grid, 1, wx.EXPAND | wx.ALL, 5) 
        self.grid = grid 

        btn_exit = wx.Button(panel, -1, "Exit") 
        vbox.Add(btn_exit, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 10) 

    #Proceed CTRL+ENTER as newline in the cell editor
    def on_frame_char_hook(self, event): 

        if event.CmdDown() and event.GetKeyCode() == wx.WXK_RETURN: 
            if self.grid.editor.IsCreated(): 
                self.grid.editor.StartingKey(event) 
            else: 
                event.Skip 
        else: 
            event.Skip()


if __name__ == "__main__": 
    app = wx.PySimpleApp() 
    f = MyFrame() 
    f.Center() 
    f.Show() 
    app.MainLoop() 
