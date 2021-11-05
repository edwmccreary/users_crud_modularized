from flask_app import app
from flask_app.controllers import user_controller
# import all of your controllers into here
# from flask_app.controllers import [name of controller file]

if __name__=="__main__":
    app.run(debug=True)