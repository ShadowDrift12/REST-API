from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Post {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }