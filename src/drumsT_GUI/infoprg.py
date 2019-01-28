#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#
#########################################################
# Name: infoprg.py
# Porpose: Show Version, Copyright, Description, etc
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: Gianluca Pernigoto <jeanlucperni@gmail.com>
# License: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Created: 13 Dec. 2017
# Rev (00)
#########################################################

import wx
from src.drumsT_DATA.data_info import prg_info

info_rls = prg_info()# calling
#-----------------#
NAME = info_rls[0]
PRG_NAME = info_rls[1]
VERSION = info_rls[2]
RELEASE = info_rls[3]
COPYRIGHT = info_rls[4]
WEBSITE = info_rls[5]
AUTHOR = info_rls[6]
MAIL = info_rls[7]
COMMENT = info_rls[8]
SHORT_DESCR = info_rls[9]
DESCRIPTION = info_rls[10]
SHORT_LIC = info_rls[11]
LONG_LIC = info_rls[12]

def info(drumsT_icon):
        """
        This part I copied entirely so. It's a predefined template to
        create a dialogue on the program information
        """

        info = wx.AboutDialogInfo()

        info.SetIcon(wx.Icon(drumsT_icon, wx.BITMAP_TYPE_PNG))

        info.SetName(NAME)

        info.SetVersion(VERSION)

        info.SetDescription(u'%s\n%s' %(SHORT_DESCR,DESCRIPTION))

        info.SetCopyright(u"%s %s" %(COPYRIGHT, AUTHOR))

        info.SetWebSite(WEBSITE)

        info.SetLicence(LONG_LIC)

        info.AddDeveloper(u"\n\n%s \n"
                          u"Mail: %s\n"
                          u"Website: %s\n\n"
                          u"%s\n" %(AUTHOR,MAIL,WEBSITE,COMMENT))

        #info.AddDocWriter(u"La documentazione ufficiale é parziale e ancora\n"
                        #u"in fase di sviluppo, si prega di contattare l'autore\n"
                        #u"per ulteriori delucidazioni.")

        #info.AddArtist(u'Gianluca Pernigotto powered by wx.Python')

        #info.AddTranslator(u"Al momento, il supporto alle traduzioni manca del\n"
                        #u"tutto, l'unica lingua presente nel programma é\n"
                        #u"quella italiana a cura di: Gianluca Pernigotto\n\n"

                        #u"Se siete interessati a tradurre il programma\n"
                        #u"in altre lingue, contattare l'autore.")

        wx.AboutBox(info)
        #event.Skip()
