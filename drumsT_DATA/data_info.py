#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: prg_info.py
# Porpose: Version, Copyright, Description, etc
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: Gianluca Pernigoto <jeanlucperni@gmail.com>
# License: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Created: 13 Dec. 2017
# Rev (00)
#########################################################

def prg_info():
    """
    General info strings for *About* and *setup.py*
    """
    Release_Name = 'DrumsT'
    Program_Name = 'drumsT'
    Version = ' v0.2.1'
    Release = 'Alpha'
    Copyright = u'© 2013-2017'
    Website = 'https://github.com/jeanslack/DrumsT'
    Author = 'Gianluca Pernigotto (aka jeanslack)'
    Mail = '<jeanlucperni@gmail.com>'
    Comment = (u"If you want to customize this program,\n"
               u"or if you need assistance, more information,\n"
               u"please, do not hesitate to contact me.")

    short_d = (u"*  Musical school management  *")

    long_d = (u"\n%s is a management school application designed\n"
              u"for drums teachers. It can handle independently\n"
              u"multiple school locations with more school years.\n"
              u"It is used to store data lists of students and\n"
              u"manage the lessons of each student who learns the\n"
              u"art of drumming.\n\n"
              u"%s is open-source and cross-platform.\n" % (Release_Name,
                                                            Release_Name))

    short_l = (u"GPL3 (Gnu Public License)")

    license = (u"Copyright - %s %s\n"
                "Author and Developer: %s\n"
                "Mail: %s\n\n"
                "%s is free software: you can redistribute\n"
                "it and/or modify it under the terms of the GNU General\n"
                "Public License as published by the Free Software\n"
                "Foundation, either version 3 of the License, or (at your\n"
                "option) any later version.\n\n"

                "%s is distributed in the hope that it\n"
                "will be useful, but WITHOUT ANY WARRANTY; without\n"
                "even the implied warranty of MERCHANTABILITY or\n" 
                "FITNESS FOR A PARTICULAR PURPOSE.\n" 
                "See the GNU General Public License for more details.\n\n"

                "You should have received a copy of the GNU General\n" 
                "Public License along with this program. If not, see\n" 
                "http://www.gnu.org/licenses/" %(Copyright,Author,Author,Mail,
                                                 Release_Name, Release_Name))

    return (Release_Name, Program_Name, Version, Release, Copyright, 
            Website, Author, Mail, Comment, short_d, long_d, short_l, license)

