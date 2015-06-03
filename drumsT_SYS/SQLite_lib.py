#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#########################################################
# Name: SQLite_lib.py
# Porpose: read/write access to databases
# Author: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GNU GENERAL PUBLIC LICENSE (see LICENSE)
# Rev (01) 18/05/2015
#########################################################

import sqlite3

class School_Class(object):
    """
    Records to a main databases index.
    Query
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
            # create a table Lesson
            cursor.execute("""CREATE TABLE Lesson
                           (IDlesson INTEGER PRIMARY KEY AUTOINCREMENT,
                           IDclass INT, Attendance TEXT, Date TEXT, 
                           Reading TEXT, Setting TEXT, Rudiments TEXT,
                           Coordination TEXT, Styles TEXT, Minusone TEXT,
                           Other1 TEXT, Other2 TEXT, Other3 TEXT, Votes TEXT,
                           Notes TEXT)
                           """)
            
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
    def lessons(self, lisT, path):
        """
        Insert a new day lesson into Lesson table
        """
        try:
            conn = sqlite3.connect('%s' % path)
            cursor = conn.cursor()
            
            #cursor.execute('SELECT max(IDyear) FROM School')# by index
            #max_id = cursor.fetchone()[0] # by index
            cursor.execute("""INSERT INTO Lesson (IDclass, Attendance, Date, 
                            Reading, Setting, Rudiments, Coordination, Styles,
                            Minusone, Other1, Other2, Other3, Votes, Notes) 
                            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                        """, [lisT[0],lisT[1],lisT[2],lisT[3],lisT[4],
                                lisT[5],lisT[6],lisT[7],lisT[8],lisT[9],
                                lisT[10],lisT[11],lisT[12],lisT[13]])
            conn.commit()
            conn.close()
        
        except sqlite3.OperationalError as err:
            self.error = True
            self.exception = ("DrumsT: Failed to lesson method\n\n"
                                "sqlite3.OperationalError: %s" % err)

        return self.error, self.exception
    #----------------------------------------------------------------------#
    def showInTable(self, IDclass, path):
        """
        Show all items class by selecting school year
        """
        conn = sqlite3.connect('%s' % (path))
        cursor = conn.cursor()

        n = cursor.execute("""SELECT * FROM Lesson WHERE IDclass=?""", [IDclass])
        
        lesson = []
        for row in n:
            lesson.append(row)

        conn.close()

        return lesson
        
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
    def change_class_item(self, Name, Surname, Phone, Address, BirthDate,
                          LevelCourse, JoinDate, IDclass, path):
        """
        Updates existing records in the Class table
        """
        conn = sqlite3.connect('%s' % path) # or use :memory: to put it in RAM
        cursor = conn.cursor()
        
        cursor.execute("""UPDATE Class SET Name=?,Surname=?,Phone=?,
                          Address=?,BirthDate=?,LevelCourse=?, JoinDate=? 
                          WHERE (IDclass=?)
                       """, [Name,Surname,Phone,Address,BirthDate,
                               LevelCourse,JoinDate, IDclass])
        conn.commit()
        conn.close()
    #----------------------------------------------------------------------#
    def change_lesson_items(self, lisT, path):
        """
        Updates existing records in the Lesson table
        """
        conn = sqlite3.connect('%s' % path) # or use :memory: to put it in RAM
        cursor = conn.cursor()

        cursor.execute("""UPDATE Lesson SET Attendance=?, Date=?, Reading=?,
                          Setting=?, Rudiments=?, Coordination=?, Styles=?,
                          Minusone=?, Other1=?, Other2=?, Other3=?, Votes=?, 
                          Notes=? 
                          WHERE (IDlesson=?)
                       """, [lisT[2],lisT[3],lisT[4],lisT[5],lisT[6],lisT[7],
                             lisT[8],lisT[9],lisT[10],lisT[11],lisT[12],
                             lisT[13],lisT[14],lisT[0]])
        conn.commit()
        conn.close()
        #----------------------------------------------------------------------#
    def delete(self, IDclass, path):
        """
        cancella records già esistenti
        """
        conn = sqlite3.connect('%s' % path) # or use :memory: to put it in RAM
        cursor = conn.cursor()
        
        
        cursor.execute("""DELETE FROM Class WHERE (IDclass=?)""", [IDclass])
        cursor.execute("""DELETE FROM Lesson WHERE (IDclass=?)""", [IDclass])
        
        conn.commit()
        conn.close()
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
        return ret
    ########################################################################

