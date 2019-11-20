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
        comment_parser.add_argument('id_product')

        args = comment_parser.parse_args()

        products = args["id_product"][1:-1].split(',')

        # Transfor it into an entry
        for id_product in products:
            current_comment = {
                                "id_product": int(id_product.strip()),
                                "comment": str(args['comment'])
                              }
            # We input the entry in the data base
            description = mongo.db.comments
            description.insert(current_comment)
            
        return 200            