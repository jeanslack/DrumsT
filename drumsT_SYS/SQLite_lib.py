#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

class Schools_Id(object):
    """
    Records to a main databases index.
    """
    
    def __init__(self):
        """
        
        """
        self.error = False
        self.exception = None
    #-------------------------------------------------------------------------#
    def newSchool(self, path, name, year):
        """
        Add new schools: the 'school' name is the name of newer table 
        with content progressive school years.
        The Students table is defined by school year names.
        Also, when run DrumsT for first time and there is nothing 
        database/path-name configured, this method set a new one.
        """
        try:
            conn = sqlite3.connect('%s/%s/%s.drtDB' % (path,name,name)) 
            cursor = conn.cursor()
            
            # create a table School
            cursor.execute("CREATE TABLE School (IDyear text)")
            # insert IDyear in school
            cursor.execute("INSERT INTO School (IDyear) VALUES(?)", (year,))

            # create a table Students
            cursor.execute("CREATE TABLE 'Students_%s' (Id INTEGER PRIMARY KEY AUTOINCREMENT, name text)" % name)
            # insert data in year
            #cursor.execute("INSERT INTO '%s' (year) VALUES(?)" % (name), (year,))
            
            conn.commit() # record stores
            conn.close() # connect close
            
        except sqlite3.OperationalError as err:
            self.error = True
            self.exception = ("DrumsT: Failed to create new database "
                      "'schools.drtDB'\nsqlite3.OperationalError: %s" % err)

        return self.error, self.exception
    #-------------------------------------------------------------------------#
    #def insert(self, path_db): # solo quando aggiungi nuove scuole
        #"""
        #inserisce un nuovo records
        #"""
        #conn = sqlite3.connect('%s/schools.drtDB' % path_db) # or use :memory: to put it in RAM
        #cursor = conn.cursor()
        
        #name = raw_input('name  ')
        #year = raw_input('year  ')

        #cursor.execute('''INSERT INTO schools VALUES(?)''',[name])
        
        ## insert data in year
        #cursor.execute("""CREATE TABLE %s (year text)""" % name)
        #cursor.execute("INSERT INTO %s VALUES ('%s')" % (name,year))
        
        #conn.commit()
        #conn.close()

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
        
        
    def query(self, path_db, name):
        conn = sqlite3.connect('%s' % path_db) # or use :memory: to put it in RAM
        
        schools = []
        cursor = conn.execute("SELECT Id, name from Students_%s" % name)
        for row in cursor:
            schools.append(row)
        conn.close()
        return schools

    def key_query(self, path_db):
        """
        ricerca nella tabella year della scuola
        """
        conn = sqlite3.connect('%s' % path_db) # or use :memory: to put it in RAM
        
        schools = []
        cursor = conn.execute("SELECT IDyear from school")
        for row in cursor:
            schools.append(row)
        conn.close()
        return schools
        
    
        
    def add_date(self, path_db,name):
        conn = sqlite3.connect('%s/schools.drtDB' % path_db) # or use :memory: to put it in RAM
        cursor = conn.cursor()
        
        year = raw_input('year  ')
        # insert data in year
        cursor.execute("INSERT INTO %s VALUES ('%s')" % (name,year))
        
        conn.commit()
        conn.close()
        
    def insert(self,name,address,birth_dates,phone,date,level,path_db, schoolname):
        """
        inserisce un nuovo records
        """
        conn = sqlite3.connect(path_db)
        cursor = conn.cursor()
        
        #name = raw_input('name  ')
        #address = raw_input('address  ')
        #birth_dates = raw_input('birth_dates  ')
        #phone = raw_input('phone  ')
        #phone = raw_input('joined_date  ')
        #level = raw_input('level  ')
        
        #cursor.execute('''INSERT INTO students VALUES(?,?,?,?,?,?)''', 
        #[name,address,birth_dates,phone,date,level])
        cursor.execute('''INSERT INTO Students_%s (name) VALUES(?)''' % (schoolname), [name])
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
