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
        Create new School and Class tables: 
        The 'School' table has one only column with IDyear.
        The Class table is defined by own ID and IDyear of the school.
        Also, this method is used when run DrumsT for first time and there 
        is nothing database/path-name configured, this method set a new one.
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
            
            cursor.execute("""CREATE TABLE Students 
                           (IDclass INT, Attendance TEXT, Date TEXT, Lessons TEXT
                           )""")
            
            conn.commit() # record stores
            conn.close() # connect close
            
        except sqlite3.OperationalError as err:
            self.error = True
            self.exception = ("DrumsT: Failed to create new database\n\n"
                              "sqlite3.OperationalError: %s" % err)

        return self.error, self.exception
    
    #-----------------------------------------------------------------------#
    def checkstudent(self, Name, Surname, path, IDyear):
        """
        This method must be used before the insertstudent() method to 
        test if there are existance profiles with same match by 
        name and surname.
        """
        conn = sqlite3.connect('%s' % path)
        cursor = conn.cursor()
        
        ctrl = cursor.execute("SELECT * FROM Class WHERE (IDyear=?)", [IDyear])
        for m in ctrl:
            if '%s %s' %(m[2],m[3]) == '%s %s' %(Name,Surname):
                conn.close()
                self.error = True
                self.exception = ("This name already exists:"
                                  "\n\nNAME/SURNAME:  %s %s\nPHONE:  %s\n"
                                  "ADDRESS:  %s\nBIRTHDATE:  %s\n"
                                  "JOINED DATE:  %s\nLEVEL:  %s"
                                  "\n\nWant you to save anyway?" % (
                                  m[2],m[3],m[4],m[5],m[6],m[7],m[8]))
                break
        conn.close()
        return self.error ,self.exception

    #-----------------------------------------------------------------------#
    def insertstudent(self, Name, Surname, Phone, Address, BirthDate, 
                      JoinDate, LevelCourse, path, IDyear):
        """
        Insert new student profile into Class table. Note that this add
        a only one element by call.
        """
        try:
            conn = sqlite3.connect('%s' % path)
            cursor = conn.cursor()
        
            #cursor.execute('SELECT max(IDyear) FROM School')# by index
            #max_id = cursor.fetchone()[0] # by index
            cursor.execute("""INSERT INTO Class (IDyear,Name,Surname,Phone,
                                Address,BirthDate,LevelCourse, JoinDate) 
                                VALUES(?,?,?,?,?,?,?,?)
                            """, [IDyear,Name,Surname,Phone,Address,BirthDate,
                                    LevelCourse,JoinDate])
            
            conn.commit()
            conn.close()
            
        except sqlite3.OperationalError as err:
            self.error = True
            self.exception = ("DrumsT: Failed to insertclass\n\n"
                                "sqlite3.OperationalError: %s" % err)

        return self.error, self.exception

    #----------------------------------------------------------------------#
    def lessons(self, Attendance, date, Lessons, path, IDclass,):
        conn = sqlite3.connect('%s' % path)
        cursor = conn.cursor()
        
        #cursor.execute('SELECT max(IDyear) FROM School')# by index
        #max_id = cursor.fetchone()[0] # by index
        cursor.execute("""INSERT INTO Students (IDclass, Attendance,Date, 
                       Lessons) VALUES(?,?,?,?)
                       """, [IDclass,Attendance,date,Lessons])

        conn.commit()
        conn.close()
        
    #-------------------------------------------------------------------------#
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
    def displaystudent(self, IDclass, path):
        """
        Show all items schools by in the combobox school year
        """
        conn = sqlite3.connect('%s' % (path))
        cursor = conn.cursor()
        
        student = []
        n = cursor.execute("""SELECT * FROM Students WHERE IDclass=?""", [IDclass])
        for row in n:
            student.append(row)
            
        conn.close()
        print student
        return student
        
    #----------------------------------------------------------------------#
    def updateyear(self, path, year):
        """
        Insert new date in School if not still exist
        """
        conn = sqlite3.connect('%s' % (path))
        cursor = conn.cursor()
        
        # find a match error
        ctrl = cursor.execute("SELECT * FROM School WHERE IDyear=?", [year])
        for m in ctrl:
            if year == m[0]:
                conn.close()
                self.error = True
                return self.error

        # insert year in school
        cursor.execute("INSERT INTO School (IDyear) VALUES(?)", [year])
        
        conn.commit()
        conn.close()
        
        return self.error
    #----------------------------------------------------------------------#
    def search_all(self, long_name, path_db):
        conn = sqlite3.connect('%s/students.drtDB' % path_db) # or use :memory: to put it in RAM
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
        return re
    ########################################################################
    def update(self, path):
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
