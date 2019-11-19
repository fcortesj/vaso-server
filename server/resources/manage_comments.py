from flask_restful import Resource, reqparse
from resources.imports import mongo

class Comments(Resource):
    """ Class used to post and get comments of a specified product(s)"""

    def post(self):
        """
        Adds comment to the database.
        It parses the received JSON and transforms it into an entry.
        """
        # Get Json object elements
        comment_parser = reqparse.RequestParser()
        comment_parser.add_argument('comment')
        comment_parser.add_argument('id_product', action='append')

        args = comment_parser.parse_args()
        # Transfor it into an entry
        for id_product in args['id_product']:
            current_comment = {
                                "id_product": str(id_product),
                                "comment": str(args['comment'])
                              }
            # We input the entry in the data base
            description = mongo.db.comments
            description.insert(current_comment)
            
        return 200            