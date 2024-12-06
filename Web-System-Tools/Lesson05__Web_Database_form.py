# THIS PROJECT IS AN EXAMPLE APP. SOME CODE MAY NOT BE ACTUALLY USEFUL
# FOR DEMONSTRATION PURPOSES ONLY
# YOUR MILEAGE MAY VARY
# Requirements are Flask, Flask-WTF, Flask-SQLAlchemy

import os

from flask import (Flask,
                   Blueprint,
                   redirect,
                   render_template_string,
                   request,
                   url_for)

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import func
from wtforms import StringField, SubmitField, TextField
from wtforms.validators import Required

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

settings = {
    'SECRET_KEY': 'super not secure development key',
    'DEBUG': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + os.path.join(BASE_PATH,
                                                           'posts.db'),
    'SQLALCHEMY_ECHO': True
}

app = Flask(__name__)
db = SQLAlchemy(app)

app.config.update(settings)

blog = Blueprint('blog', __name__)

# The following are template strings which contain html with jinja tags.
# Jinja2 is a template language which uses a specific tags within text that can
# parse text and execute python code.

# The index template string for the main page
index_template = '''
{% if posts %}
    <table class="posts-table">
        <thead>
            <tr>
                <th>ID</th>
                <th>title</th>
                <th>likes</th>
                <th>like?</th>
            </tr>
        </thead>
        <tbody>
        {% for post in posts %}
            <tr>
                <td>{{ post.id }}</td>
                <td>{{ post.title }}</td>
                <td{% if post.likes | length > 3 %} style="color:green;"{% endif %}>{{ post.likes | length }}</td>
                <td><a href="{{ url_for('blog.like_post', post_id=post.id) }}">like it!</a>
            </tr>
        {% endfor %}
        </tbody>
    </table>
{% else %}
<p> You don't have any posts </p>
{% endif %}
<a href = "{{ url_for('blog.create_post') }}">Create Post</a>
'''

# The template string for creating a blog post
create_post_template = '''
<form action="{{ url_for('blog.create_post') }}" method="POST" name="post_form">
    {{ form.csrf_token }}
    {{ form.title.label }}
    {{ form.title }}
    {{ form.text.label }}
    {{ form.text }}
    {{ form.submit() }}
</form>
'''

error_template = '''
<div id="error">
    <h1> Sorry, there was an error</h1>
    <p>Error:# {{ status_code }}</p>
</div>
'''


# Create the form
class CreatePostForm(FlaskForm):
    """
    The form used to create a blog post
    """
    title = StringField('Title', validators=[Required()])
    text = TextField('Text', validators=[Required()])
    submit = SubmitField('Submit')


# Create the Models
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.Text())

    likes = db.relationship('PostLike')

    @classmethod
    def all(cls):
        """
        Returns all researcher items from the database
        """
        return db.session.query(cls).all()


class PostLike(db.Model):
    __tablename__ = 'post_likes'

    id = db.Column(db.Integer(), primary_key=True)
    post_id = db.Column(db.Integer(), db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    users = db.relationship('User')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return self.name

    @classmethod
    def get_random(cls):
        user = db.session.query(cls).order_by(func.random()).first()
        return user.id


# Register errorhandlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template_string(error_template, status_code=404), 404


@app.errorhandler(500)
def server_error(e):
    return render_template_string(error_template, status_code=500), 500


# Create the routes
@blog.route('/', methods=['GET'])
def index():
    posts = Post.all()
    return render_template_string(index_template, posts=posts)


@blog.route('/create', methods=['GET', 'POST'])
def create_post():
    form = CreatePostForm(request.form)
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    text=form.text.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.index'))
    return render_template_string(create_post_template, form=form)


@blog.route('/like/<int:post_id>')
def like_post(post_id):
    post = db.session.query(Post).get(post_id)
    user = db.session.query(User).get(1)
    post_like = db.session.query(PostLike).filter(PostLike.user_id == user.id).first()
    if post_like:
        # A post was found with that user so redirect back.
        # We would typically flash a message giving an error.
        return redirect(url_for('index'))
    else:

        post_like = PostLike(post_id=post.id,
                             user_id=User.get_random())
        db.session.add(post_like)
        db.session.commit()
        return redirect(url_for('blog.index'))


app.register_blueprint(blog)


# Utils
def create_and_seed_db():
    db.create_all()

    for x in range(10):
        user = User(name='user' + str(x))
        db.session.add(user)
    db.session.commit()

    return


if __name__ == '__main__':
    # This will create the database if it doesn't already exist.
    if os.path.exists(app.config['SQLALCHEMY_DATABASE_URI'].split('///')[1]):
        app.run()
    else:
        create_and_seed_db()
        app.run()
