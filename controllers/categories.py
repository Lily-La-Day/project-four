from flask import Blueprint
from models.category import Category, CategorySchema


api = Blueprint('categories', __name__)
category_schema = CategorySchema()


@api.route('/categories', methods=['GET'])
def show_categories():
    categories = Category.query.all()
    return category_schema.jsonify(categories, many=True), 200

@api.route('/categories/<int:category_id>', methods=['GET'])
def filter_categories(category_id):
    category = Category.query.get(category_id)
    print(category.writings)
    return category_schema.jsonify(category), 200
