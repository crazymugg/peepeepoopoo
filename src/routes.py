from flask import render_template, redirect, request

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
            db.create_all()
        return redirect('/')
    
    @app.route('/team/<name>')
    def create_team(name):
        team = models['Team'](name=name)
        db.session.add(team)
        db.session.commit()
        return redirect('/')
    

    @app.route('/game/<name>')
    def create_game(name):
        game = models['Game'](name=name)
        db.session.add(game)
        db.session.commit()
        return redirect('/')
    

    @app.route('/teamgame')
    def create_teamgame():
        team  = request.args.get('team', None)
        game  = request.args.get('game', None)
        teamgame = models['TeamGame'](team_id = team, game_id = game)
        db.session.add(teamgame)
        db.session.commit()
        return redirect('/')