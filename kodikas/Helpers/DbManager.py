#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      3o Εσπερινο ΕΠΑΛ
#
# Created:     22/02/2019
#-------------------------------------------------------------------------------
import sqlite3
print (sqlite3.sqlite_version)
from sqlite3 import Error


class DbManager:
    def __init__(self,filePath):
        self.filePath=filePath
        self.lastQuery=''

        try:
            self.conn = sqlite3.connect(filePath)
            #self.conn.execute('''CREATE TABLE Person
            # ([id] INTEGER PRIMARY KEY,[name] text,[surname] text,[imagepath] text, [isauthorised] integer, [lastseen] date)''')

# Create table - COUNTRY
        except Error as e:
            print(e)
            print ("Cannot connect to database")

    def runSelect(self,query):
        self.lastQuery=query
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        return rows



#a=DbManager("robot2.sqlite")
#persons=a.runSelect("SELECT * FROM Person")
#print (persons)
