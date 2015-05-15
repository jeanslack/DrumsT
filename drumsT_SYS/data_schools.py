#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

#print sys.argv

def create_new():
    # create a table
    conn = sqlite3.connect("/home/gianluca/Pubblici/Project_github/GestionaleDrums/mydatabase.db") # or use :memory: to put it in RAM
    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE schools
                (name text, year text)""")

    choice = raw_input('Insert one record (1) or more records (*)')

    if choice == '1':
        cursor.execute("INSERT INTO schools VALUES ('Modern Drums Istitute', '14/Febbraio/2016')")

        # save data to database
        conn.commit()
        
    elif choice == '*':
        # insert multiple records using the more secure "?" method
        schools = [('Barbarano medie', '2013/2014'),
                ('Privatamente', '2014/2015'),
                ('Tregnago', '2012/2013')]
        cursor.executemany("INSERT INTO schools VALUES (?,?)", schools)
        conn.commit()
        
    else:
        print 'error'
    
    
def update_year():
    """
    aggiorna records già esistenti
    """
    conn = sqlite3.connect("/home/gianluca/Pubblici/Project_github/GestionaleDrums/mydatabase.db") # or use :memory: to put it in RAM
    cursor = conn.cursor()
    
    choice1 = raw_input('Name school to change: ')
    choice2 = raw_input('New name of the school: ')
    
    sql = """
    UPDATE schools 
    SET year = '%s' 
    WHERE year = '%s'
    """ % (choice1, choice2)
    
    cursor.execute(sql)
    conn.commit()
    
def update_name():
    """
    aggiorna records già esistenti
    """
    conn = sqlite3.connect("/home/gianluca/Pubblici/Project_github/GestionaleDrums/mydatabase.db") # or use :memory: to put it in RAM
    cursor = conn.cursor()
    
    choice1 = raw_input('Name school to change: ')
    choice2 = raw_input('New name of the school: ')
    
    sql = """
    UPDATE schools 
    SET name = '%s' 
    WHERE name = '%s'
    """ % (choice1, choice2)
    
    cursor.execute(sql)
    conn.commit()
    
def delete():
    """
    cancella records già esistenti
    """
    conn = sqlite3.connect("/home/gianluca/Pubblici/Project_github/GestionaleDrums/mydatabase.db") # or use :memory: to put it in RAM
    cursor = conn.cursor()
    
    choice_del = raw_input('School name to delete: ')
    sql = """
    DELETE FROM schools
    WHERE name = '%s'
    """ % (choice_del)
    cursor.execute(sql)
    conn.commit()
    
    
def query():
    conn = sqlite3.connect("/home/gianluca/Pubblici/Project_github/GestionaleDrums/mydatabase.db") # or use :memory: to put it in RAM
    cursor = conn.cursor()
    
    sql = "SELECT * FROM schools WHERE name=?"
    cursor.execute(sql, [("2012/2013")])
    #print cursor.fetchall()  # or use fetchone()
    print cursor.fetchone()  # or use fetchone()
    
    print "\nHere's a listing of all the records in the table:\n"
    for row in cursor.execute("SELECT rowid, * FROM schools ORDER BY name"):
        print row
            
    print "\nResults from a LIKE query:\n"
    sql = """
    SELECT * FROM schools 
    WHERE year LIKE 'The%'"""
    cursor.execute(sql)
    print cursor.fetchall()
    

       


if sys.argv[1] == "create":
    create_new()
elif sys.argv[1] == "update":
    update()
elif sys.argv[1] == "delete":
    delete()
elif sys.argv[1] == "query":
    query()
elif sys.argv[1] == "":
    print 'Null'
