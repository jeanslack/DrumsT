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
    #err = False
    msg = ("A new drumsT rootdir has been created:"
           "\n\n%s\n\nYou must re-start the "
           "DrumsT application now.\n\nGood Work !" % path)
    try:
        F = open('%s/.drumsT/drumsT.conf' %(DIRNAME),'r').readlines()
    except IOError as error:
        #raise # WARNING: use raise statement for debug only
        print (error)
        #err = True
        msg = ("DrumsT: Failed to write drumsT.conf:\n\n"
               "ERROR: %s" % error)
        return True, msg
    else:
        data = F
        for a in data:
            if a.startswith('DATABASE_PATH_NAME='):
                match = a
                data = [w.replace(match, 'DATABASE_PATH_NAME=%s\n' % (path)) 
                        for w in data
                        ]
    finally:
        F = open('%s/.drumsT/drumsT.conf' %(DIRNAME),'r').close()
    
    with open('%s/.drumsT/drumsT.conf' %(DIRNAME),'w') as Fw:
        for i in data:
            overwrite = Fw.write('%s' % i)
    return False, msg
#--------------------------------------------------------------------------#
def create_rootdir(path,name):
    """
    Prepare a root dir for database during first time running 
    or when create another school
    """
    err = False
    msg = None
    #if os.path.exists('%s' % path):
    if os.path.exists('%s/%s' % (path,name)):
        err = True
        msg = ("DrumsT: Already exist : %s" % path)
        return err, msg
    try:
        os.makedirs('%s/%s' % (path,name))

    except OSError as error:
        err = True
        msg = ("DrumsT: Failed to make database root dir\n\nOSError: %s" % error)
        print (error)
        
    return err, msg
#--------------------------------------------------------------------------#
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
