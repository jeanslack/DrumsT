#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from wx.lib import wordwrap
import wx.grid


class CutomGridCellAutoWrapStringRenderer(wx.grid.PyGridCellRenderer):   
    def __init__(self): 
        wx.grid.PyGridCellRenderer.__init__(self)

    def Draw(self, grid, attr, dc, rect, row, col, isSelected):
        text = grid.GetCellValue(row, col)
        dc.SetFont( attr.GetFont() ) 
        text = wordwrap.wordwrap(text, grid.GetColSize(col), dc, breakLongWords = False)
        hAlign, vAlign = attr.GetAlignment()       
        if isSelected: 
            bg = grid.GetSelectionBackground() 
            fg = grid.GetSelectionForeground() 
        else: 
            bg = attr.GetBackgroundColour()
            fg = attr.GetTextColour() 
        dc.SetTextBackground(bg) 
        dc.SetTextForeground(fg)
        dc.SetBrush(wx.Brush(bg, wx.SOLID))
        dc.SetPen(wx.TRANSPARENT_PEN)
        dc.DrawRectangleRect(rect)            
        grid.DrawTextRectangle(dc, text, rect, hAlign, vAlign)

    def GetBestSize(self, grid, attr, dc, row, col): 
        text = grid.GetCellValue(row, col)
        dc.SetFont(attr.GetFont())
        text = wordwrap.wordwrap(text, grid.GetColSize(col), dc, breakLongWords = False)
        w, h, lineHeight = dc.GetMultiLineTextExtent(text)                   
        return wx.Size(w, h)        

    def Clone(self): 
        return CutomGridCellAutoWrapStringRenderer() 
