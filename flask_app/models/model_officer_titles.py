from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class OfficerTitle:
    def __init__( self , data ):
        self.id = data['id']
        self.officer_title = data['officer_title']
    
    # C - Create methods / INSERT a new entry into a table
    
    # R - Read methods / return data from table
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM officer_role_names;"
        results = connectToMySQL(DATABASE).query_db(query)
        officers = [] 
        for officer in results:
            officers.append( cls(officer) )
        return officers  # Returns a list of class instances

    # U - Update methods / UPDATE existing entries with new values

    # D - Delete methods / DELETE existing entries from table
    