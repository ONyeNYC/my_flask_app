from flask import request, jsonify
from .models import Item
from . import create_app

app = create_app()

@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'error': 'Bad request'}), 400
    item = Item.create(name=request.json['name'])
    return jsonify(item.id), 201

@app.route('/items', methods=['GET'])
def get_items():
    items = list(Item.select().dicts())
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.get_or_none(Item.id == item_id)
    if item:
        item.delete_instance()
        return jsonify({}), 204
    return jsonify({'error': 'Not found'}), 404
