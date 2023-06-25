from flask import render_template, redirect

def create_routes(app, db) -> None:
    @app.route('/')
    def index():
        return render_template('home.html')
    
    @app.route('/about')
    def about():
        return render_template('about.html')
    
    @app.route('/dbreset')
    def dbreset():
        with app.app_context():
            db.drop_all()
        with app.app_context():
            db.create_all()
        return redirect('/')