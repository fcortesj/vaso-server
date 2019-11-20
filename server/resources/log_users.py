from flask_restful import Resource, reqparse
from resources.imports import mongo
from flask import abort

class Log_Users(Resource):
    """ 
        This class manage the users log in 
        If it exists returns approval else returns error message
    """
    
    def post(self):
        # First we create the parser of the elements involved
        log_user_parser = reqparse.RequestParser()
        log_user_parser.add_argument('username')
        log_user_parser.add_argument('password')

        #We serach in the database for the user
        args = log_user_parser.parse_args()
        current_query = list(mongo.db.users.find({ 'username' : str(args['username'])}, { 'password' : str(args['password'])}))

        #Then if the user exists we return the username and the name if not we return an error
        if not current_query:
            return abort(409)
        else:
            return { "username": str(args['username'])}
