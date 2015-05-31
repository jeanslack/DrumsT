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
path_db = '/home/gianluca/annuncio/drumsT_DB/drums_co/drums_co.drtDB'
from drumsT_SYS.SQLite_lib import School_Class 

Name = u'gino'
Surname = u'kurletto'
Phone = u'234'
Address = u'via margera'
BirthDate = u'de febbraio dai'
LevelCourse = u'basilare'
JoinDate = u'el sette'
IDclass = u'1'

lessons = School_Class().change_class_item(Name,Surname,Phone,Address,BirthDate,
                                     LevelCourse,JoinDate, IDclass,path_db)

