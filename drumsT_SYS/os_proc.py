#!/usr/bin/python
# -*- coding: UTF-8 -*- 
#
#########################################################
# Name: os_proc.py
# Porpose: Common operative system processing
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (01) 18/05/2015
#########################################################

import os

DIRNAME = os.path.expanduser('~') # /home/user

#--------------------------------------------------------------------------#
def write_newpath(path):
    """
    Write file configuration for new database path.
    This function is called when first time run or if 
    user change path-name for database
    """
    F = open('%s/.drumsT/drumsT.conf' %(DIRNAME),'r').readlines()
    data = F
    F = open('%s/.drumsT/drumsT.conf' %(DIRNAME),'r').close()

    #print data
    for a in data:
        if a.startswith('DATABASE_PATH_NAME='):
            match = a
            
    data = [w.replace(match, 'DATABASE_PATH_NAME=%s\n' % (path)) 
            for w in data
            ]

    F = open('%s/.drumsT/drumsT.conf' %(DIRNAME),'w')
    for i in data:
        overwrite = F.write('%s' % i)

    F.close()
    
#--------------------------------------------------------------------------#
def create_rootdir(path,name,year):
    """
    Prepare a root dir for database during first time running 
    or when create another school with name and year
    """
    try: # if exist dir not exit OSError, go...
        os.makedirs('%s/DrumsT_DataBases/%s/%s' % (path,name,year))

    except OSError:
        return "Failed"
