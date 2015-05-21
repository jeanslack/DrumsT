#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
#import sqlite3 as lite
import sys 

def inserting_1():
    """
    These two lines insert two cars into the table. Using the with keyword, 
    the changes are automatically committed. Otherwise, we would have to 
    commit them manually.
    """
    con = None
    
    path = '/home/gianluca/Experimenti/provaSQlite'
    
    school = 'Barbarano'
    
    try:
        con = sqlite3.connect('%s/test.db' % path)
        cur = con.cursor()
        
        cur.execute("CREATE TABLE '%s'(Year TEXT)" % school)
        cur.execute("INSERT INTO '%s' VALUES('2014_2015')" % school)
        cur.execute("INSERT INTO '%s' VALUES('2015_2016')" % school)
        
        cur.execute("CREATE TABLE students_2014_2015(IDstudent INT, name TEXT, surname TEXT)")
        cur.execute("INSERT INTO students_2014_2015 VALUES(1,'marco', 'gambirasio')")
        cur.execute("INSERT INTO students_2014_2015 VALUES(2,'luca', 'rossi')")
        
        cur.execute("CREATE TABLE students_2015_2016(IDstudent INT, name TEXT, surname TEXT)")
        cur.execute("INSERT INTO students_2015_2016 VALUES(1,'marco', 'gambirasio')")
        cur.execute("INSERT INTO students_2015_2016 VALUES(2,'luca', 'rossi')")
        
        
        cur.execute("CREATE TABLE luca_rossi_2014_2015_id1(studi TEXT)")
        cur.execute("INSERT INTO luca_rossi_2014_2015_id1 VALUES('studio dei rudimenti')")
        
        cur.execute("CREATE TABLE marco_gambirasio_2014_2015_id2(studi TEXT)")
        cur.execute("INSERT INTO marco_gambirasio_2014_2015_id2 VALUES('studio dei rudimenti')")
        
        cur.execute("CREATE TABLE luca_rossi_2015_2016_id1(studi TEXT)")
        cur.execute("INSERT INTO luca_rossi_2015_2016_id1 VALUES('solfeggio')")
        
        cur.execute("CREATE TABLE marco_gambirasio_2015_2016_id2(studi TEXT)")
        cur.execute("INSERT INTO marco_gambirasio_2015_2016_id2 VALUES('solfeggio ritmico')")

    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
         
    finally:
       if con:
           con.close()
           
            
def inserting_2():
    """
    These two lines insert two cars into the table. Using the with keyword, 
    the changes are automatically committed. Otherwise, we would have to 
    commit them manually.
    """
    
    path = '/home/gianluca/Experimenti/provaSQlite'
    school = 'Barbarano'
    
    con = lite.connect('%s/test.db' % path)
    
    
    with con:
        cur = con.cursor()
        
        #cur.execute("CREATE TABLE '%s'(Year TEXT)" % school)
        #cur.execute("INSERT INTO '%s' VALUES('2014_2015')" % school)
        #cur.execute("INSERT INTO '%s' VALUES('2015_2016')" % school)
        
        cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
        cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
        cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
        cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
        cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
        cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
        cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
        cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
        cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")
        
        #cur.execute("CREATE TABLE students_2014_2015(IDstudent INT, name TEXT, surname TEXT)")
        #cur.execute("INSERT INTO students_2014_2015 VALUES(1,'marco', 'gambirasio')")
        #cur.execute("INSERT INTO students_2014_2015 VALUES(2,'luca', 'rossi')")
        
        #cur.execute("CREATE TABLE students_2015_2016(IDstudent INT, name TEXT, surname TEXT)")
        #cur.execute("INSERT INTO students_2015_2016 VALUES(1,'marco', 'gambirasio')")
        #cur.execute("INSERT INTO students_2015_2016 VALUES(2,'luca', 'rossi')")
        
        
        #cur.execute("CREATE TABLE luca_rossi_2014_2015_id1(studi TEXT)")
        #cur.execute("INSERT INTO luca_rossi_2014_2015_id1 VALUES('studio dei rudimenti')")
        
        #cur.execute("CREATE TABLE marco_gambirasio_2014_2015_id2(studi TEXT)")
        #cur.execute("INSERT INTO marco_gambirasio_2014_2015_id2 VALUES('studio dei rudimenti')")
        
        #cur.execute("CREATE TABLE luca_rossi_2015_2016_id1(studi TEXT)")
        #cur.execute("INSERT INTO luca_rossi_2015_2016_id1 VALUES('solfeggio')")
        
        #cur.execute("CREATE TABLE marco_gambirasio_2015_2016_id2(studi TEXT)")
        #cur.execute("INSERT INTO marco_gambirasio_2015_2016_id2 VALUES('solfeggio ritmico')")
           
def retrieving_data():
    con = None
    
    try:    
        con = sqlite3.connect('test.db')
        cur = con.cursor()    
        cur.execute("SELECT * FROM Cars")
        
        rows = cur.fetchall()
        
        for row in rows:
            print row
            
    except sqlite3.Error, e:
        print "Error: %s" % e.args[0]
        sys.exit(1)
        
    finally:
       if con:
           con.close()
        
        
#retrieving_data()
inserting_1()
#inserting_2()
