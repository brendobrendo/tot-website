from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from datetime import datetime
from flask import flash, session

class Poast:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.content = data['content']
        self.member_first_name = data['first_name']
        self.member_last_name = data['last_name']
        self.poast_date = data['updated_at'].strftime("%B %d, %Y")
        self.member_id = data['members.id']
    
    # C - Create methods / INSERT a new entry into a table
    @classmethod
    def save(cls, data):
        query = "INSERT INTO poasts (title, content, member_id) VALUES (%(title)s, %(content)s, %(member_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # R - Read methods / return data from table
    @classmethod
    def get_all(cls):
        query = "SELECT poasts.id, members.first_name, members.last_name, members.id, poasts.title, poasts.content, poasts.updated_at FROM poasts JOIN members ON poasts.member_id = members.id ORDER BY poasts.id DESC LIMIT 20;"
        results = connectToMySQL(DATABASE).query_db(query)
        members = [] 
        for member in results:
            members.append( cls(member) )
        return members  # Returns a list of class instances

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM members WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])  # Uses member id to return an instance of the class

    # U - Update methods / UPDATE existing entries with new values

    @classmethod
    def update_one(cls, data):
        query = 'UPDATE poasts SET title=%(title)s, content=%(content)s, member_id=%(member_id)s WHERE id=%(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    # D - Delete methods / DELETE existing entries from table
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM poasts WHERE id= %(id)s;"
        return connectTomMySQL(DATABASE).query_db(query, data)

    