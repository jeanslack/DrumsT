#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import with_statement
import sqlite3
#import sqlite3 as lite
import sys 


#def retrieving_data():
    #con = None
    
    #try:    
        #con = sqlite3.connect('/home/gianluca/Documenti/drumsT_DB/Barbarano/Barbarano.drtDB')
        #cur = con.cursor()    
        #cur.execute("SELECT * FROM Class")
        
        #rows = cur.fetchall()
        
        #for row in rows:
            #print row
            
    ##except sqlite3.Error, e:
    #except Exception, e:
        #print "Error: %s" % e.args[0]
        #sys.exit(1)
        
    #finally:
       #if con:
           #con.close()
           




#db_filename = '/home/gianluca/Documenti/drumsT_DB/Barbarano/Barbarano.drtDB'
#def retrieving_data():
    #with sqlite3.connect(db_filename) as conn:
        
        #try:
            
            ## Insert
            #cur = conn.cursor()
            #cur.execute("SELECT * FROM Class")
            
            #rows = cur.fetchal()
            
            #for row in rows:
                #print row
        
        #except Exception, err:
            ## Discard the changes
            #print 'ERROR:', err
            
#retrieving_data()



db_filename = '/ome/gianluca/Documenti/drumsT_DB/Barbarano/Barbarano.drtDB'

def retrieving_data():
    try:
        #conn = sqlite3.connect(db_filename)
        with sqlite3.connect(db_filename) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Class")
            
            rows = cur.fetchall()
            
            for row in rows:
                print row
                
    except Exception, err: # parent of IOError, OSError *and* WindowsError where available
        print 'ERROR:', err
        #raise
            
retrieving_data()
