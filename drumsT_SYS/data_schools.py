#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

class Schools_Names(object):
    """
    """
    def __init__(self):
        """
        """

    def create_new(self, path): # quando crei tutto nuovo e non esiste ancora nessun database
        
        name = raw_input('Insert name school  ')
        date = raw_input('Year  ')
        
        
        
        conn = sqlite3.connect('%s/schools.drtDB' % path) # or use :memory: to put it in RAM
        cursor = conn.cursor()
        # create a table school
        cursor.execute("""CREATE TABLE schools (name text)""")
        # insert name in schools
        cursor.execute("INSERT INTO schools VALUES ('%s')" % name)
        
        # create a table year
        cursor.execute("""CREATE TABLE %s (year text)""" % name)
        # insert data in year
        cursor.execute("INSERT INTO %s VALUES ('%s')" % (name,date))


        conn.commit()

    
    
    def update_year(self, path):
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
    
    def update_name(self, path):
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
    
    def delete(self, path):
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
        
        
    def query(self, path_db):
        conn = sqlite3.connect('%s/schools.drtDB' % path_db) # or use :memory: to put it in RAM
        
        schools = []
        cursor = conn.execute("SELECT name from schools")
        for row in cursor:
            schools.append(row)
        conn.close()
        return schools

    def key_query(self, path_db, key): # ricerca nella tabella year della scuola
        conn = sqlite3.connect('%s/schools.drtDB' % path_db) # or use :memory: to put it in RAM
        
        schools = []
        cursor = conn.execute("SELECT year from %s" % key)
        for row in cursor:
            schools.append(row)
        conn.close()
        return schools
        
    def insert(self, path_db): # solo quando aggiungi nuove scuole
        """
        inserisce un nuovo records
        """
        conn = sqlite3.connect('%s/schools.drtDB' % path_db) # or use :memory: to put it in RAM
        cursor = conn.cursor()
        
        name = raw_input('name  ')
        year = raw_input('year  ')

        cursor.execute('''INSERT INTO schools VALUES(?)''',[name])
        
        # insert data in year
        cursor.execute("""CREATE TABLE %s (year text)""" % name)
        cursor.execute("INSERT INTO %s VALUES ('%s')" % (name,year))
        
        conn.commit()
        conn.close()
        
    def add_date(self, path_db,name):
        conn = sqlite3.connect('%s/schools.drtDB' % path_db) # or use :memory: to put it in RAM
        cursor = conn.cursor()
        
        year = raw_input('year  ')
        # insert data in year
        cursor.execute("INSERT INTO %s VALUES ('%s')" % (name,year))
        
        conn.commit()
        conn.close()
    
    
#add_date('/home/gianluca/Pubblici/Project_github/DrumsT/test/DrumsT_DataBases', 'Barbarano')
#insert('/home/gianluca/Pubblici/Project_github/DrumsT/test/DrumsT_DataBases')
#create_new('/home/gianluca/Pubblici/Project_github/DrumsT/test/DrumsT_DataBases')
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
