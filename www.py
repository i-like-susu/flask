from application import app
from index_control import index_page


app.register_blueprint(index_page, url_prefix='/')