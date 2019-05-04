#-------------------------------------------------------------------------------
# Name:        DbManager
# Purpose:
#
# Author:      3o Εσπερινο ΕΠΑΛ
#
# Created:     22/02/2019
#-------------------------------------------------------------------------------

#συνδέεται με sqlite3 και τρέχει wql
import sqlite3
print (sqlite3.sqlite_version)
from sqlite3 import Error


class DbManager:
    def __init__(self,filePath):
        self.filePath=filePath #το μονοπάτι της βάσης
        self.lastQuery='' #το τελευταίο query

        try:
            self.conn = sqlite3.connect(filePath) #δοκίμασε να συνδεθείς
            #self.conn.execute('''CREATE TABLE Person
            # ([id] INTEGER PRIMARY KEY,[name] text,[surname] text,[imagepath] text, [isauthorised] integer, [lastseen] date)''')

# Create table - COUNTRY
        except Error as e: #αν λάθος τύπωσε
            print(e)
            print ("Cannot connect to database")

    def runSelect(self,query): # Εκτέλεση query
        self.lastQuery=query
        cur = self.conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()  #πάρε τις γραμμές
        return rows #επέστρεψε τις



