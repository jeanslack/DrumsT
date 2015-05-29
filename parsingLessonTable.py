#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: lesson_prospective.py
# Porpose: Show all data lessons of a one student
# Author: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (00) 28/05/2015
#########################################################

IDclass = 1
path_db = '/home/gianluca/annuncio/drumsT_DB/Cinzano_music/Cinzano_music.drtDB'
from drumsT_SYS.SQLite_lib import School_Class 

lessons = School_Class().showInTable(IDclass, path_db)

#print lessons

for n, item in enumerate(lessons):
    print n, item[0]

