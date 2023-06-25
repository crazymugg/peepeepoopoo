def create_models(db) -> dict:
    models = {}
    
    class Game(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        year = db.Column(db.Integer, nullable=True)
        week = db.Column(db.Integer, nullable=True)
        game_num = db.Column(db.Integer, nullable=True)
        #serial_id = '' 2022_01_05
        team_a = db.Column(db.String, nullable=True)
        team_b = db.Column(db.String, nullable=True)
        lines = db.relationship('Line', backref='game', lazy='selectin')
    models['Game'] = Game

    class Line(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=True)
        quarter = db.Column(db.Integer, nullable=True)
        time = db.Column(db.Integer, nullable=True)
        game_num = db.Column(db.Integer, nullable=True)
        team_a_score = db.Column(db.Integer, nullable=True)
        team_b_score = db.Column(db.Integer, nullable=True)
    models['Line'] = Line
        
    class Team(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String, nullable=True)
    models['Team'] = Team


    return models