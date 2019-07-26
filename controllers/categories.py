from flask import Blueprint
from models.category import Category, CategorySchema


api = Blueprint('categories', __name__)
category_schema = CategorySchema()


@api.route('/categories', methods=['GET'])
def show_categories():
    categories = Category.query.all()
    return category_schema.jsonify(categories, many=True), 200
