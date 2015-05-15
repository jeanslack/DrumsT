#!/usr/bin/python
# -*- coding: UTF-8 -*- 
#
#########################################################
# Name: boot.py
# Porpose: Check OS type and configuration files
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Rev (01) 15/05/2015
#########################################################

"""
All controls for establish the operative systems type and controls 
for verify the integrity and changes on the configuration files of 
drumsT and parsing for configuration file has centralized here.
"""
import sys
import os
import shutil
import platform

#work current directory (where are drumsT?):
PWD = os.getcwd()
#current user directory:
DIRNAME = os.path.expanduser('~') # /home/user

########################################################################
# CONTROLS CONFIGURATION FILE AND PARSINGS
########################################################################
def control_config():
    """
    This function is for check existing drumsT.conf in ~/.videomass. 
    It is called in drumsT.py. If these files do not exist or are deleted 
    in ~/, this function restore them from assign paths established below. 
    Check which operating system is in use to make changes necessary. 
    Also, assign the paths of icons.
    """
    copyerr = False

    # What is OS ??
    if sys.platform.startswith('darwin'):
        OS = 'darwin'

    elif sys.platform.startswith('linux2'):
        OS = 'linux2'
        
    elif sys.platform.startswith('win'):
        OS = 'windows'
        
    else:
        OS = sys.platform
    """
    Assignment path where there is videomass.conf
    This depends if portable mode or installable mode:
    """
    if os.path.exists('%s/drumsT_GUI' % (PWD)) or sys.platform.startswith('darwin'):
        """
        This paths are for portable mode in ?NIX Systems
        """
        main_path = '%s/share' % PWD
        # Icons:
        drumsT_icon = "%s/art/drumsT.png" % PWD
        openStudent_icon = '%s/art/openStudent.png' % PWD
        addStudent_icon = '%s/art/addStudent.png' % PWD
        changeStudent_icon = '%s/art/changeStudent.png' % PWD
        delStudent_icon = '%s/art/delStudent.png' % PWD
        #help_icon = '%s/art/help.png' % PWD
    else:
        """
        This paths are only for installable mode in linux2
        """
        main_path = '/usr/share/drumsT/config'
        # Icons:
        drumsT_icon = "/usr/share/pixmaps/drumsT.png"
        openStudent_icon = '/usr/share/drumsT/icons/openStudent.png'
        addStudent_icon = '/usr/share/drumsT/icons/addStudent.png'
        changeStudent_icon = '/usr/share/drumsT/icons/changeStudent.png'
        delStudent_icon = '/usr/share/drumsT/icons/delStudent.png'
        #help_icon = '/usr/share/drumsT/icons/help.png'

    if os.path.exists('%s/.drumsT' % DIRNAME):

        if os.path.isfile('%s/.drumsT/drumsT.conf' % DIRNAME):
            pass
        else:
            shutil.copyfile('%s/drumsT.conf' % main_path, 
                            '%s/.drumsT/drumsT.conf' % DIRNAME)
    else:
        
        try: # if exist folder ~/.videomass
            shutil.copytree(main_path, '%s/.drumsT' % DIRNAME)
            
        except OSError:
            copyerr = True

    return (drumsT_icon, openStudent_icon, addStudent_icon, changeStudent_icon, 
            delStudent_icon, OS, main_path, copyerr)


def parser_fileconf():
    """
    execute a parsing on drumsT.conf.
    This parser system not evaluate the rows and columns for 
    reading specific lines. The only limit is that the name 
    of the variables should never be changed.
    """
    conf = '%s/.drumsT/drumsT.conf' % (DIRNAME)
    
    uncomment = []

    fconf = open(conf, 'r')
    list_lines = fconf.readlines()
    fconf.close()

    for line in list_lines:
        if not line.startswith('#'):
            # strip remove all \n + spaces and tab
            uncomment.append(line.strip())
    """
    remove empty string from a list:

                cleaned = filter(None, uncomment)

    Note however, that filter returns a list in Python 2, but a generator 
    in Python 3. You will need to convert it into a list in Python 3 :

                cleaned = list(filter(None, uncomment)) 
                
    or use the list comprehension solution:
    """
    cleaned = [x for x in uncomment if x]

    if cleaned == []:
        ret = 'error' # corrupted
        
    else:
        for item in cleaned:
            if item.startswith('DATABASE_PATH_NAME='):
                path_db = item

        if path_db[19:] == '':
            ret = 'empty' # first state of program
        else:
            ret = path_db[19:].strip()
    return ret
