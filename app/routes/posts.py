from flask import Blueprint, jsonify, request
from app import db
from app.models.post import Post

bp = Blueprint('posts', __name__, url_prefix='/posts')

@bp.route('/', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])

@bp.route('/', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(title=data['title'], content=data['content'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.to_dict()), 201

@bp.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get(post_id)
    if post:
        return jsonify(post.to_dict())
    else:
        return jsonify({'error': 'Post not found'}), 404

@bp.route('/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.get(post_id)
    if post:
        data = request.get_json()
        post.title = data['title']
        post.content = data['content']
        db.session.commit()
        return jsonify(post.to_dict())
    else:
        return jsonify({'error': 'Post not found'}), 404

@bp.route('/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Post not found'}), 404