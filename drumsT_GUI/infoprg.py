#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx

def info(drumsT_icon):
        """
        This part I copied entirely so. It's a predefined template to
        create a dialogue on the program information
        
        """
        description = (u"DrumsT is a management school application designed\n"
                       u"for drums teachers. It can handle independently\n"
                       u"multiple school locations with more school years.\n"
                       u"It is used to store data lists of students and\n"
                       u"manage the lessons of each student who learns the\n"
                       u"art of drumming.\n\n"
                       u"DrumsT is open-source and cross-platform.\n"
                       u"For more info, please visit our site.")

        licence = (u"Copyright © 2015-2016 Gianluca Pernigotto\n"
                "Author and Developer: Gianluca Pernigotto\n"
                "Mail: <jeanlucperni@gmail.com>\n\n"
                "DrumsT is free software: you can redistribute\n"
                "it and/or modify it under the terms of the GNU General\n"
                "Public License as published by the Free Software\n"
                "Foundation, either version 3 of the License, or (at your\n"
                "option) any later version.\n\n"

                "DrumsT is distributed in the hope that it\n"
                "will be useful, but WITHOUT ANY WARRANTY; without\n"
                "even the implied warranty of MERCHANTABILITY or\n" 
                "FITNESS FOR A PARTICULAR PURPOSE.\n" 
                "See the GNU General Public License for more details.\n\n"

                "You should have received a copy of the GNU General\n" 
                "Public License along with this program. If not, see\n" 
                "http://www.gnu.org/licenses/")

        info = wx.AboutDialogInfo()

        info.SetIcon(wx.Icon(drumsT_icon, wx.BITMAP_TYPE_PNG))
        
        info.SetName('DrumsT')
        
        info.SetVersion(' v0.1.0')
        
        info.SetDescription(description)
        
        info.SetCopyright(u'(C) 2015-2016 Gianluca Pernigotto (aka jeanslack)')
        
        info.SetWebSite(u'https://github.com/jeanslack/DrumsT')
        
        info.SetLicence(licence)
        
        info.AddDeveloper(u"\n\nGianluca Pernigotto, (aka jeanslack) \n"
                        u"Mail: <jeanlucperni@gmail.com>\n"
                        u"Web Page: https://github.com/jeanslack/DrumsT\n\n"
                        u"If you like it, please write us\n")
                        
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
