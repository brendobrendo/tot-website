from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class RoleConfirmation:
    def __init__( self , data ):
        self.id = data['id']
        self.response_id = data['response_id']  # 1='confirmed' 2='need a volunteer'
    
    # C - Create methods / INSERT a new entry into a table
    @classmethod
    def confirm_role(cls, data):
        query = "INSERT INTO role_confirmation_responses (response_id, role_assignment_id) VALUES (1, %(role_assignment_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def need_volunteer(cls, data):
        query = "INSERT INTO role_confirmation_responses (response_id) VALUES (2, %(role_assignment_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)


    # R - Read methods / return data from table
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM role_confirmation_statuses;"
        results = connectToMySQL(DATABASE).query_db(query)
        confirmations = [] 
        for confirmation in results:
            confirmations.append( cls(confirmation) )
        return confirmations  # Returns a list of class instances

    # U - Update methods / UPDATE existing entries with new values
    @classmethod
    def update_confirmation(cls, data):
        pass

    # D - Delete methods / DELETE existing entries from table
    @classmethod
    def delete_confirmation(cls, data):
        pass