#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

class School_Class(object):
    """
    Records to a main databases index.
    """
    
    def __init__(self):
        """
        
        """
        self.error = False
        self.exception = None
    #-------------------------------------------------------------------------#
    def newSchoolyear(self, path, name, year):
        """
        Add new schools: the 'School' name is the name of newer table 
        with content progressive  IDyears.
        The Class table is defined by own IDclass and IDyear of the school.
        Also, when run DrumsT for first time and there is nothing 
        database/path-name configured, this method set a new one.
        """
        try:
            conn = sqlite3.connect('%s/%s/%s.drtDB' % (path,name,name)) 
            cursor = conn.cursor()
            
            # create a table School
            cursor.execute("""CREATE TABLE School (IDyear TEXT)""")
            # insert year in school
            cursor.execute("INSERT INTO School (IDyear) VALUES(?)", [year])

            # create a table Class
            cursor.execute("""CREATE TABLE Class 
                           (IDclass INTEGER PRIMARY KEY AUTOINCREMENT, 
                           IDyear INT, Name TEXT, Surname TEXT, Phone TEXT,
                           Address TEXT, BirthDate TEXT, JoinDate TEXT, 
                           LevelCourse TEXT)
                           """)
            
            conn.commit() # record stores
            conn.close() # connect close
            
        except sqlite3.OperationalError as err:
            self.error = True
            self.exception = ("DrumsT: Failed to create new database\n\n"
                              "sqlite3.OperationalError: %s" % err)

        return self.error, self.exception
    
    #-----------------------------------------------------------------------#
    def insertclass(self, Name, Surname, Phone, Address, BirthDate, 
                    JoinDate, LevelCourse, path, IDyear):
        """
        Insert data Class
        """
        try:
            conn = sqlite3.connect('%s' % path)
            cursor = conn.cursor()

            #cursor.execute('SELECT max(IDyear) FROM School')
            #max_id = cursor.fetchone()[0]
            cursor.execute("""INSERT INTO Class (IDyear,Name,Surname,Phone,
                        Address,BirthDate,LevelCourse, JoinDate) 
                        VALUES(?,?,?,?,?,?,?,?)""", [IDyear,Name,Surname,
                                                        Phone,Address,BirthDate,
                                                        LevelCourse,JoinDate])
            conn.commit()
            conn.close()
            
        except sqlite3.OperationalError as err:
            self.error = True
            self.exception = ("DrumsT: Failed to insertclass\n\n"
                              "sqlite3.OperationalError: %s" % err)

        return self.error, self.exception
        
        
        
    #----------------------------------------------------------------------#
    def displayclass(self, path, IDyear):
        """
        Show all items class by selecting school year
        """
        conn = sqlite3.connect('%s' % (path))
        cursor = conn.cursor()

        n = cursor.execute("""SELECT * FROM Class WHERE IDyear=?""", [IDyear])
        
        student = []
        for row in n:
            student.append(row)

        conn.close()

        return student

    #----------------------------------------------------------------------#
    def displayschool(self, path):
        """
        Show all items schools by in the combobox school year
        """
        conn = sqlite3.connect('%s' % (path))
        
        schools = []
        cursor = conn.execute("SELECT * from School")
        for row in cursor:
            schools.append(row)
        conn.close()
        return schools
    
    #----------------------------------------------------------------------#
    def add_date(self, path, year):
        """
        Insert new date in School if not still exist
        """
        conn = sqlite3.connect('%s' % (path))
        cursor = conn.cursor()

        # insert year in school
        cursor.execute("INSERT INTO School (IDyear) VALUES(?)", [year])
        
        conn.commit()
        conn.close()
    ########################################################################
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

    
        
    
        
    
        
    
    
#a = School_Class()
#a.insert()
#a.display_class()
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
