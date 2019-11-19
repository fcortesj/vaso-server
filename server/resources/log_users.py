from flask_restful import Resource, reqparse
from resources.imports import mongo

class Log_Users(Resource):
    """ 
        This class manage the users log in 
        If it exists returns approval else returns error message
    """
    
    def post(self):
        # First we create the parser of the elements involved
        log_user_parser = reqparse.RequestParser()
        log_user_parser.add_argument("username")
        log_user_parser.add_argument("password")

        args = log_user_parser.parse_args()
        current_query = mongo.db.Users.find({"$and": [{"Users": {'username': args['username']}}, 
                                                  {"Users": {'password': args['password']}}
                                                 ]
                                        }
                                       )
        print(current_query)