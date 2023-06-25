from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)

    @app.route('/')
    def index():
        return render_template('base.html')
    
    @app.route('/about')
    def about():
        return render_template('about.html')

    return app