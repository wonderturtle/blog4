from flask import Blueprint

# Blueprint definition
blog = Blueprint("blog", __name__, template_folder = '/flaskr/blueprints/blog/templates', url_prefix = '/user/blog')


from flaskr.blueprints.blog import routes