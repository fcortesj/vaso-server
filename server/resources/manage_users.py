from flask_restful import Resource, reqparse
from resources.imports import mongo 

class Manage_Users(Resource):
    """ Class implemented to manage users (Sign In)"""

    def post(self):
        """
            Adds new user to the database
        """

        # First we create the parser and then we add the input fields
        user_parser = reqparse.RequestParser()
        user_parser.add_argument('name')
        user_parser.add_argument('age')
        user_parser.add_argument('city')
        user_parser.add_argument('address')
        user_parser.add_argument('email')
        user_parser.add_argument('cel')
        user_parser.add_argument('username')
        user_parser.add_argument('password')

        # We parse the arguments
        args = user_parser.parse_args()

        # We check if the username already exists in the db if not we add the new entry
        user_list = list(mongo.db.users.find({ 'username' : str(args['username'])}))
    
        if not user_list:

            signed_user = {
                            "name"    : str(args['name']),
                            "age"     : str(args['age']),
                            "city"    : str(args['city']),
                            "address" : str(args['address']),
                            "email"   : str(args['email']),
                            "cel"     : str(args['cel']),
                            "username": str(args['username']),
                            "password": str(args['password'])
                          }

            description = mongo.db.users
            description.insert(signed_user)

            return { "username": str(args['username']) , "name": str(args['name']) }

        else:

            return 409

            
