from MySQLConnection import connectToMySQL

class User:
    def __init__(self, id, first_name, last_name, email, created_at, updated_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_db").query_db( query )
        return results

