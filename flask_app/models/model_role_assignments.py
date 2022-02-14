from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from datetime import datetime

class RoleAssignment:
    def __init__( self , data ):
        self.id = data['id']
        self.member_first_name = data['first_name']
        self.member_last_name = data['last_name']
        self.meeting_date = data['meeting_date'].strftime("%B %d, %Y")
        self.role_name = data['name']
        self.member_id = data['members.id']
        self.response_id = data['response_id']
    
    # C - Create methods 
    @classmethod
    def save(cls, data):
        query = "INSERT INTO role_assignments (role_name, member_id, meeting_id, role_name_id) VALUES ('blue', %(member_id)s, %(meeting_id)s, %(role_name_id)s );"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    # R - Read methods / return data from table
    @classmethod
    def get_upcoming_user(cls, data):
        query = "SELECT role_assignments.id, role_names.name, meetings.meeting_date, members.first_name, members.last_name, members.id, role_confirmation_responses.response_id FROM role_assignments JOIN role_names ON role_assignments.role_name_id = role_names.id JOIN meetings ON role_assignments.meeting_id = meetings.id JOIN members ON role_assignments.member_id = members.id LEFT JOIN role_confirmation_responses ON role_assignments.id = role_confirmation_responses.role_assignment_id WHERE meetings.meeting_date >= CURRENT_DATE() AND role_assignments.member_id = %(member_id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        role_assignments = [] 
        for role_assignment in results:
            role_assignments.append( cls(role_assignment) )
        return role_assignments  # Returns a user's upcoming role assignments as a list of instances

    @classmethod
    def get_upcoming_meeting(cls, data):
        query = "SELECT role_assignments.id, role_names.name, meetings.meeting_date, members.first_name, members.last_name, members.id, role_confirmation_responses.response_id FROM role_assignments JOIN role_names ON role_assignments.role_name_id = role_names.id JOIN meetings ON role_assignments.meeting_id = meetings.id JOIN members ON role_assignments.member_id = members.id LEFT JOIN role_confirmation_responses ON role_assignments.id = role_confirmation_responses.role_assignment_id WHERE meetings.meeting_date >= CURRENT_DATE() AND role_assignments.meeting_id = %(meeting_id)s; "
        results = connectToMySQL(DATABASE).query_db(query, data)
        role_assignments = []
        for role_assignment in results:
            role_assignments.append( cls(role_assignment) )
        return role_assignments  # Returns role assignments for a specific meeting as a list of instances

    @classmethod
    def get_all(cls):
        query = "SELECT role_assignments.id, role_names.name, meetings.meeting_date, members.first_name, members.last_name, members.id, role_confirmation_responses.response_id FROM role_assignments JOIN role_names ON role_assignments.role_name_id = role_names.id JOIN meetings ON role_assignments.meeting_id = meetings.id LEFT JOIN role_confirmation_responses ON role_assignments.id = role_confirmation_responses.role_assignment_id JOIN members ON role_assignments.member_id = members.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        role_assignments = []
        for role_assignment in results:
            role_assignments.append( cls(role_assignment))
        return role_assignments



    # U - Update methods / UPDATE existing entries with new values
    @classmethod
    def update_one(cls, data):
        query = 'UPDATE role_assignments SET member_id=%(member_id)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    
    # D - Delete methods / DELETE existing entries from table
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM role_assignments WHERE id= %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

   


