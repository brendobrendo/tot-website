from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Member:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.memberid = data['memberid']
        self.officer_key = data['officer_role_name_id']
    
    # C - Create methods / INSERT a new entry into a table
    @classmethod
    def save(cls, data):
        query = "INSERT INTO members (first_name, last_name, email, password, memberid) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, 111111);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # R - Read methods / return data from table
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM members LEFT JOIN officer_assignments ON members.id = officer_assignments.member_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        members = [] 
        for member in results:
            members.append( cls(member) )
        return members  # Returns a list of class instances

    @classmethod
    def get_last_one(cls):
        query = "SELECT * FROM member LEFT JOIN officer_assignments ON members.id = officer_assignments.member_id ORDER BY id DESC LIMIT 1;"
        result = connectToMySQL(DATABASE).query_db(query)
        return cls(result)  # Returns an instance of a Member class based on last member entered into the db

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM members LEFT JOIN officer_assignments ON members.id = officer_assignments.member_id WHERE members.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])  # Uses member id to return an instance of the class

    @classmethod
    def get_one_email(cls, data):
        query = 'SELECT * FROM members LEFT JOIN officer_assignments ON members.id = officer_assignments.member_id WHERE email = %(email)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return False # This returns an intance of the class or False if email is not found or data not input correctly


    # U - Update methods / UPDATE existing entries with new values

    @classmethod
    def update_one(cls, data):
        query = 'UPDATE members SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    # D - Delete methods / DELETE existing entries from table
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM members WHERE id= %(id)s;"
        return connectTomMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_member(data):
        is_valid = True

        if len(data['first_name']) < 2:
            flash("First name must be 2 characters", "err_members_first_name")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name must be 2 characters", "err_members_last_name")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address", "err_members_email")
            is_valid = False  
        else:
            member = Member.get_one_email(data)
            if member:
                flash("Email account already in use", "err_members_email")
                is_valid = False  
        if len(data['password']) < 8:
            flash("Your password needs to be at least 8 characters", "err_members_password")
            is_valid = False
        if data['password'] != data['confirmation_password']:
            flash("Your passwords do not match", "err_password_match")
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True
        
        if len(data['email']) < 2:
            flash("Email must be at least 2 characters", "err_members_email_login")
            is_valid = False

        elif not EMAIL_REGEX.match(data['email']):
            flash("Must enter a valid email address", "err_members_email_login")
            is_valid = False  

        else:
            member = Member.get_one_email(data)
            print(data, "this is the data in the else clause")
            print(type(member), "this is the type of member")
            if member:
                if not bcrypt.check_password_hash(member.password, data['password']):
                    flash("Invalid credentials", "err_members_password_login")
                    print(data['password'], "is datapassword")
                    print(member.password, "is member.password")
                    is_valid = False
                else:
                    session['user_id'] = member.id

        print(is_valid, "IS_VALID LOGIN")
        return is_valid




