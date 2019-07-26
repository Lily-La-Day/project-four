from app import app
from controllers import writings, writers, editors, edits, finals, categories

app.register_blueprint(writings.api, url_prefix='/api')
app.register_blueprint(writers.api, url_prefix='/api')
app.register_blueprint(editors.api, url_prefix='/api')
app.register_blueprint(edits.api, url_prefix='/api')
app.register_blueprint(finals.api, url_prefix='/api')
app.register_blueprint(categories.api, url_prefix='/api')
