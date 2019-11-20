"""
Flask based server for back-ended purposes of the proyect.

It uses Flask library to behave like a rest api
"""
from resources.imports import app, api
from resources.manage_comments import Comments
from resources.manage_users import Manage_Users
from resources.log_users import Log_Users


api.add_resource(Manage_Users, '/manage_users')
api.add_resource(Comments, '/manage_comments')
api.add_resource(Log_Users, '/log_users')

if __name__=="__main__":
    app.run(port=8080, host='0.0.0.0')