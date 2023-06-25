from flask import render_template, redirect

def create_routes(app, db, models) -> None:
    @app.route('/')
    def index():
        # country_query = models['Country'].query.order_by(models['Country'].name)
        results = models['Team'].query.order_by(models['Team'].name)
        print(results)
        return render_template('home.html', results=results)
    
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
    
    @app.route('/team/<name>')
    def create(name):
        team = models['Team'](name=name)
        db.session.add(team)
        db.session.commit()
        return redirect('/')