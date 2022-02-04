from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash, session
import re

class RoleName:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
    
    # C - Create methods / INSERT a new entry into a table
    
    # R - Read methods / return data from table
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM role_names;"
        results = connectToMySQL(DATABASE).query_db(query)
        role_names = [] 
        for role_name in results:
            role_names.append( cls(role_name) )
        return role_names  # Returns a list of class instances


    # U - Update methods / UPDATE existing entries with new values

    # D - Delete methods / DELETE existing entries from table

   