#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys

#print sys.argv

def create_new(path):
    # create a table
    conn = sqlite3.connect('%s/schools.drtDB' % path) # or use :memory: to put it in RAM
    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE schools
                (name text, year text)""")

    choice = raw_input('Insert one record (1) or more records (*)')

    if choice == '1':
        cursor.execute("INSERT INTO schools VALUES ('Barbarano medie', '2016_2017')")

        # save data to database
        conn.commit()
        
    elif choice == '*':
        # insert multiple records using the more secure "?" method
        schools = [('Barbarano medie', '2013_2014'),
                ('Privatamente', '2014_2015'),
                ('Tregnago', '2012_2013')]
        cursor.executemany("INSERT INTO schools VALUES (?,?)", schools)
        conn.commit()
        
    else:
        print 'error'
    
    
def update_year(path):
    """
    aggiorna records già esistenti
    """
    conn = sqlite3.connect('%s/schools.drtDB' % path) # or use :memory: to put it in RAM
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
    
def update_name(path):
    """
    aggiorna records già esistenti
    """
    conn = sqlite3.connect('%s/schools.drtDB' % path) # or use :memory: to put it in RAM
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
    
def delete(path):
    """
    cancella records già esistenti
    """
    conn = sqlite3.connect('%s/schools.drtDB' % path) # or use :memory: to put it in RAM
    cursor = conn.cursor()
    
    choice_del = raw_input('School name to delete: ')
    sql = """
    DELETE FROM schools
    WHERE name = '%s'
    """ % (choice_del)
    cursor.execute(sql)
    conn.commit()
    
    
def query(path_db):
    conn = sqlite3.connect('%s/schools.drtDB' % path_db) # or use :memory: to put it in RAM
    
    schools = []
    cursor = conn.execute("SELECT name, year from schools")
    for row in cursor:
        schools.append(row)
    conn.close()
    print schools
    return schools
    
def insert(path_db):
    """
    inserisce un nuovo records
    """
    conn = sqlite3.connect('%s/schools.drtDB' % path_db) # or use :memory: to put it in RAM
    cursor = conn.cursor()
    
    name = raw_input('name  ')
    year = raw_input('year  ')

    
    cursor.execute('''INSERT INTO schools VALUES(?,?)''', 
                   [name,year])
    conn.commit()
    conn.close()
    
    
    
#insert('/home/gianluca/Documenti/DrumsT_DataBases')

#if sys.argv[1] == "create":
    #create_new()
#elif sys.argv[1] == "update":
    #update()
#elif sys.argv[1] == "delete":
    #delete()
#elif sys.argv[1] == "query":
    #query()
#elif sys.argv[1] == "":
    #print 'Null'
