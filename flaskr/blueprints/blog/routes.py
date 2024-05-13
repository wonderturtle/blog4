from flaskr.blueprints.blog import blog
from flask import render_template
from flaskr import login_manager
from flask_login import login_user, login_required, logout_user, current_user
from flaskr.models.user import User




@blog.route('/')
def view():
  posts = [  # Simulate some blog posts
      {'title': 'Post 1', 'content': 'Content for post 1'},
      {'title': 'Post 2', 'content': 'Content for post 2'}
  ]
  return render_template('blog/index.html', posts=posts, title = 'Blog')