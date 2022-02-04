from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from datetime import datetime

class Meeting:
    def __init__( self , data ):
        self.id = data['id']
        self.meeting_date = data['meeting_date'].strftime("%B %d, %Y")
        self.meeting_location = data['name']
    
    # C - Create methods / INSERT a new entry into a table
    @classmethod
    def save(cls, data):
        query = "INSERT INTO meetings (meeting_location_id, meeting_date, meeting_date_id) VALUES (%(meeting_location_id)s, %(meeting_date)s, 5 );"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # R - Read methods / return data from table
    @classmethod
    def get_all(cls):
        query = "SELECT meetings.id, meetings.meeting_date, meeting_locations.name FROM meetings JOIN meeting_locations ON meetings.meeting_location_id = meeting_locations.id WHERE meetings.meeting_date >= CURRENT_DATE() ORDER BY meetings.meeting_date;"
        results = connectToMySQL(DATABASE).query_db(query)
        meetings = [] 
        for meeting in results:
            meetings.append( cls(meeting) )
        return meetings  # Returns a list of class instances

    @classmethod
    def get_next(cls):
        query = "SELECT meetings.id, meetings.meeting_date, meeting_locations.name FROM meetings JOIN meeting_locations ON meetings.meeting_location_id = meeting_locations.id WHERE meetings.meeting_date >= CURRENT_DATE() ORDER BY meetings.meeting_date LIMIT 1;"
        result = connectToMySQL(DATABASE).query_db(query)
        return cls(result[0])  # Returns the next meeting as a class instance

    # U - Update methods / UPDATE existing entries with new values
    @classmethod
    def update_one(cls, data):
        query = 'UPDATE meetings SET meeting_date=%(meeting_date)s, meeting_location_id=%(meeting_location_id)s, meeting_date_id=5 WHERE id=%(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    # D - Delete methods / DELETE existing entries from table
    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM meetings WHERE id= %(id)s;"
        return connectTomMySQL(DATABASE).query_db(query, data)

    
