#def create_new(path_db):
## create a table
#conn = sqlite3.connect(path_db) # or use :memory: to put it in RAM
#conn.row_factory = sqlite3.Row
#cursor = conn.cursor()

    #cursor.execute("""CREATE TABLE students
    #(name text, address text, birth_dates text, phone text, joined_date text, level_course text)""")
      
      #choice = raw_input('Insert one record (1) or more records (*)')
    
    #if choice == '1':
    #cursor.execute("INSERT INTO students VALUES ('Ennio Morricone','via nani n78 Lobia VR','09/12/1986', '328 234 678', '01/09/2015', 'advanced')")
    
    ## save data to database
    #conn.commit()
    
    #elif choice == '*':
    ## insert multiple records using the more secure "?" method
    #name = [('Luca Burato','via crepuscolo n34 San bonifacio VR','12/12/1973', '328 222 333', '01/09/2015', 'base'),
    #('Martino Vittori','viale foscolo 12a Verona','04/03/1980', '340 345 678', '01/09/2015', 'base'),
      #('Maria Scola','via Praissola n 23 San Bonifacio','15/05/1979', '045 889945', '01/09/2015', 'intermedio')]
        #cursor.executemany("INSERT INTO students VALUES (?,?,?,?,?,?)", name)
        #conn.commit()
        
        #else:
            #print 'error' 
            
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
################################################
def versione_1():
    con = None

    try:
        con = lite.connect('test.db')
        
        cur = con.cursor()    
        cur.execute('SELECT SQLITE_VERSION()')
        
        data = cur.fetchone()
        
        print "SQLite version: %s" % data                
        
    except lite.Error, e:
        
        print "Error %s:" % e.args[0]
        sys.exit(1)
        
    finally:
        
        if con:
            con.close()
###############################################
def version_2():
    con = lite.connect('test.db')
    
    with con:
        
        cur = con.cursor()    
        cur.execute('SELECT SQLITE_VERSION()')
        
        data = cur.fetchone()
        
        print "SQLite version: %s" % data
#################################################
def inserting_data():
    """
    These two lines insert two cars into the table. Using the with keyword, 
    the changes are automatically committed. Otherwise, we would have to 
    commit them manually.
    """
    #con = lite.connect('test.db')
    path = '/home/gianluca/Experimenti/provaSQlite'
    school = 'Barbarano'
    
    con = lite.connect('%s/test.db' % path)

    with con:
        
        cur = con.cursor()    
        cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
        cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
        cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
        cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
        cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
        cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
        cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
        cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
        cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")
inserting_data()
########################################################
"""
We verify the written data with the sqlite3 tool. First we modify the way 
the data is displayed in the console. We use the column mode and turn on 
the headers. 
"""
#    sqlite3 test.db (o nome db)
#    sqlite> .tables (lista tutte le tabelle)
#    sqlite> .exit (esce da sqlite)
#    sqlite> .mode column  
#    sqlite> .headers on
#    sqlite> SELECT * FROM Cars;
#######################################################
def last_inserted_row_id():
    con = lite.connect(':memory:')
    #con = lite.connect('test.db')

    with con:
        
        cur = con.cursor()    
        cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")
            
        lid = cur.lastrowid
        print "The last Id of the inserted row is %d" % lid
####################################################################
def retrieving_data():
    
    con = lite.connect('test.db')
    with con:    
        
        cur = con.cursor()    
        cur.execute("SELECT * FROM Cars")
        
        rows = cur.fetchall()
        
        for row in rows:
            print row
#########################################################
def retrieving_onebyone():
    con = lite.connect('test.db')

    with con:
        
        cur = con.cursor()    
        cur.execute("SELECT * FROM Cars")

        while True:
        
            row = cur.fetchone()
            
            if row == None:
                break
                
            print row[0], row[1], row[2]
###################################################
def dictionary_cursor():
    con = lite.connect('test.db')    
    
    with con:
        
        con.row_factory = lite.Row
        
        cur = con.cursor() 
        cur.execute("SELECT * FROM Cars")
        
        rows = cur.fetchall()
        
        for row in rows:
            print "%s %s %s" % (row["Id"], row["Name"], row["Price"])
##################################################
def parameterized_queries_1():
    uId = 1
    uPrice = 62300 
    
    con = lite.connect('test.db')
    
    with con:
        
        cur = con.cursor()    
        
        cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))        
        con.commit()
        
        print "Number of rows updated: %d" % cur.rowcount
################################################
def parameterized_queries_2():
    uId = 4
    
    con = lite.connect('test.db')
    
    with con:
        
        cur = con.cursor()    
        
        cur.execute("SELECT Name, Price FROM Cars WHERE Id=:Id", 
        {"Id": uId})        
        con.commit()
        
        row = cur.fetchone()
        print row[0], row[1]
################################################
"""
    METADATA

    Metadata is information about the data in the database. Metadata in a SQLite 
    contains information about the tables and columns, in which we store data. 
    Number of rows affected by an SQL statement is a metadata. Number of rows 
    and columns returned in a result set belong to metadata as well.

    Metadata in SQLite can be obtained using the PRAGMA command. SQLite objects 
    may have attributes, which are metadata. Finally, we can also obtain specific 
    metatada from querying the SQLite system sqlite_master table. 
"""
def get_metadata():
    con = lite.connect('test.db')
    
    with con:
        
        cur = con.cursor()    
        
        cur.execute('PRAGMA table_info(Cars)')
        
        data = cur.fetchall()
        
        for d in data:
            print d[0], d[1], d[2]
#####################################################            
def print_all():
    con = lite.connect('test.db')
    
    with con:
        
        cur = con.cursor()    
        cur.execute('SELECT * FROM Cars')
        
        col_names = [cn[0] for cn in cur.description]
        
        rows = cur.fetchall()
        
        print "%2s %-9s %s" % (col_names[0], col_names[1], col_names[2])
        
        for row in rows:    
            print "%2s %-9s %s" % row
###################################################
def  list_all_tables():
    con = lite.connect('test.db')
    
    with con:
        
        cur = con.cursor()    
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        
        rows = cur.fetchall()
        
        for row in rows:
            print row[0]
#########################################
def export_data():
    cars = (
                (1, 'Audi', 52643),
                (2, 'Mercedes', 57642),
                (3, 'Skoda', 9000),
                (4, 'Volvo', 29000),
                (5, 'Bentley', 350000),
                (6, 'Hummer', 41400),
                (7, 'Volkswagen', 21600)
            )
    
    def writeData(data):
        
        f = open('cars.sql', 'w')
    
        with f:
            f.write(data)
        
        
    con = lite.connect(':memory:')
    
    with con:
        
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Cars")
        cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
        cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
        cur.execute("DELETE FROM Cars WHERE Price < 30000")
        
        data = '\n'.join(con.iterdump())
        
        writeData(data)
#####################################
def import_data():
    
    def readData():
        f = open('cars.sql', 'r')
    
        with f:
            data = f.read()
            return data
    
    
    con = lite.connect(':memory:')
    
    with con:   
        
        cur = con.cursor()
        
        sql = readData()
        cur.executescript(sql)
        
        cur.execute("SELECT * FROM Cars")
    
        rows = cur.fetchall()
        
        for row in rows:
            print row
