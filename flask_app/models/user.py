from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def read_all_users(cls):
        query = "SELECT * FROM users ORDER BY id DESC"
        db_users = connectToMySQL("users_db").query_db(query)
        users = []

        for user in db_users:
            users.append(User(user))
        
        return users

    @classmethod
    def create_user(cls,data):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s)"
        return connectToMySQL("users_db").query_db(query,data)
    
    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL("users_db").query_db(query,data)

    @classmethod
    def read_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        user = connectToMySQL("users_db").query_db(query,data)
        return cls(user[0])

    @classmethod
    def update_user(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s"
        return connectToMySQL("users_db").query_db(query,data)