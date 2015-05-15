#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

#print sys.argv

def create_new(path_db):
    # create a table
    conn = sqlite3.connect(path_db) # or use :memory: to put it in RAM
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE students
                   (name text, address text, birth_dates text, phone text, joined_date text, level_course text)""")

    choice = raw_input('Insert one record (1) or more records (*)')

    if choice == '1':
        cursor.execute("INSERT INTO students VALUES ('Ennio Morricone','via nani n78 Lobia VR','09/12/1986', '328 234 678', '01/09/2015', 'advanced')")

        # save data to database
        conn.commit()
        
    elif choice == '*':
        # insert multiple records using the more secure "?" method
        name = [('Luca Burato','via crepuscolo n34 San bonifacio VR','12/12/1973', '328 222 333', '01/09/2015', 'base'),
                ('Martino Vittori','viale foscolo 12a Verona','04/03/1980', '340 345 678', '01/09/2015', 'base'),
                ('Maria Scola','via Praissola n 23 San Bonifacio','15/05/1979', '045 889945', '01/09/2015', 'intermedio')]
        cursor.executemany("INSERT INTO students VALUES (?,?,?,?,?,?)", name)
        conn.commit()
        
    else:
        print 'error'
        
def insert(name,address,birth_dates,phone,date,level,path_db):
    """
    inserisce un nuovo records
    """
    conn = sqlite3.connect(path_db) # or use :memory: to put it in RAM
    cursor = conn.cursor()
    
    #name = raw_input('name  ')
    #address = raw_input('address  ')
    #birth_dates = raw_input('birth_dates  ')
    #phone = raw_input('phone  ')
    #phone = raw_input('joined_date  ')
    #level = raw_input('level  ')
    
    cursor.execute('''INSERT INTO students VALUES(?,?,?,?,?,?)''', 
                   [name,address,birth_dates,phone,date,level])
    conn.commit()
    conn.close()
    
    
def update(path_db):
    """
    aggiorna records già esistenti
    """
    conn = sqlite3.connect(path_db) # or use :memory: to put it in RAM
    cursor = conn.cursor()
    
    choice1 = raw_input('Name school to change: ')
    choice2 = raw_input('New i_name of the school: ')
    
    sql = """
    UPDATE students 
    SET name = '%s' 
    WHERE name = '%s'
    """ % (choice1, choice2)
    
    cursor.execute(sql)
    conn.commit()
    
def delete(name, path_db):
    """
    cancella records già esistenti
    """
    conn = sqlite3.connect(path_db) # or use :memory: to put it in RAM
    cursor = conn.cursor()
    
    name = raw_input('School name to delete: ')
    sql = """
    DELETE FROM students
    WHERE name = '%s'
    """ % (name)
    cursor.execute(sql)
    conn.commit()
    
    
#def query():
    #conn = sqlite3.connect("/home/gianluca/Pubblici/Project_github/GestionaleDrums/mydatabase.db") # or use :memory: to put it in RAM
    #cursor = conn.cursor()
    
    #sql = "SELECT * FROM students WHERE i_name=?"
    #cursor.execute(sql, [("Luca")])
    #print cursor.fetchall()  # or use fetchone()
    
    #print "\nHere's a listing of all the records in the table:\n"
    #for row in cursor.execute("SELECT rowid, * FROM students ORDER BY i_name"):
        #print row
            
    #print "\nResults from a LIKE query:\n"
    #sql = """
    #SELECT * FROM students 
    #WHERE i_name LIKE 'The%'"""
    #cursor.execute(sql)
    #print cursor.fetchall()
    
def query(path_db):
    
    conn = sqlite3.connect(path_db) # or use :memory: to put it in RAM
    #cursor = conn.cursor()
    
    #sql = "SELECT * FROM students WHERE level_course=?"
    #cursor.execute(sql, [("base")])
    #print cursor.fetchall()  # or use fetchone() for grab first result
    ##print cursor.fetchone()  # or use fetchone()
    
    #print "\nHere's a listing of all the records in the table:\n"
    #for row in cursor.execute("SELECT rowid, * FROM students ORDER BY name"):
        #print row
            
    #print "\nResults from a LIKE query:\n"
    #sql = """
    #SELECT * FROM students 
    #WHERE name LIKE 'M%'"""
    #cursor.execute(sql)
    #print cursor.fetchall()
    students = []
    cursor = conn.execute("SELECT name, address, birth_dates, phone, joined_date, level_course  from students")
    for row in cursor:
        students.append(row)
    conn.close()
    return students

def search_all(long_name, path_db):
    conn = sqlite3.connect(path_db) # or use :memory: to put it in RAM
    cursor = conn.cursor()
    
    #sql = "SELECT * FROM students WHERE name=?, address=?"
    #cursor.execute(sql, [(name)])
    #print cursor.fetchall()  # or use fetchone() for grab first result
    #print cursor.fetchone()  # or use fetchone()
    
    sql = """
    SELECT * FROM students 
    WHERE instr(name, '%s') > 0;""" % (long_name,)
    #cursor.execute(sql, [])
    cursor.execute(sql)
    #print cursor.fetchall()
    ret = cursor.fetchall()
    return ret
    

        
#search_all('Martino Vittori')      
#insert(None,None,None,None,None,None)

#if sys.argv[1] == "create":
    #create_new()
#elif sys.argv[1] == "update":
    #update()
#elif sys.argv[1] == "delete":
    #delete()
#elif sys.argv[1] == "query":
    #query()
#elif sys.argv[1] == "insert":
    #insert()
#elif sys.argv[1] == "":
    #print 'Null' 
    
    
