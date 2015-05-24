#!/usr/bin/python
# -*- coding: UTF-8 -*- 
#
#########################################################
# Name: os_filesystem.py
# Porpose: Common operative system processing
# Author: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (01) 18/05/2015
#########################################################

import os
import re

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
def create_rootdir(path,name):
    """
    Prepare a root dir for database during first time running 
    or when create another school
    """
    err = False
    exc = None
    try:
        os.makedirs('%s/%s' % (path,name))
        
    except OSError as error:
        err = True
        exc = ("DrumsT: Failed to make database root dir\n\nOSError: %s" % error)
        print error
        
    return err, exc

def urlify(string):
    """
    Convert any string with white spaces, tabs, digits, question marks,  
    apostrophes, exclamation points, etc, in URLs satisfying for the
    filesystems and SQlite
    """
    # remove all digits 1234567890
    #a = re.sub("\d+", "", string)

    # Remove all non-word characters (everything except numbers and letters)
    b = re.sub(r"[^\w\s]", '', string)
    # Replace all runs of whitespace with a single underscore
    c = re.sub(r"\s+", '_', b)
    
    return c
