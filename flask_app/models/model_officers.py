from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Officer:
    def __init__(self, data):
        self.id = data['id']
        self.officer_first_name = data['first_name']
        self.officer_last_name = data['last_name']
        self.officer_member_id = data['members.id']
        self.title_name = data['officer_title']
        self.title_id = data['officer_role_names.id']
        self.email = data['email']

    # C - Create methods / INSERT a new entry into a table
    @classmethod
    def save(cls, data):
        query = "INSERT INTO officer_assignments (member_id, officer_role_name_id) VALUES (%(member_id)s, %(officer_role_name_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # R - Read methods / return data from table
    @classmethod
    def get_all(cls):
        query = "SELECT officer_assignments.id, members.first_name, members.last_name, members.id, members.email, officer_role_names.officer_title, officer_role_names.id FROM officer_assignments JOIN officer_role_names ON officer_assignments.officer_role_name_id = officer_role_names.id JOIN members ON officer_assignments.member_id = members.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        officers = []
        for officer in results:
            officers.append(cls(officer))
        return officers  # Returns a list of class instances

    @staticmethod
    def get_officer_ids(data):
        officer_ids = []
        for officer in data:
            officer_ids.append(officer['officer_member_id'])
        return officer_ids

    # U - Update methods / UPDATE existing entries with new values

    # D - Delete methods / DELETE existing entries from table
