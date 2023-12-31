from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.mutable import MutableList

def create_models(db) -> dict:


    # Base = declarative_base()

    # class TeamGame(Base):
    #     __tablename__ = 'teamgame'

    #     game_id = db.Column("game_id", db.ForeignKey('game.id'), primary_key=True),
    #     team_id = db.Column("team_id", db.ForeignKey('team.id'), primary_key=True)



    # # TeamGame = db.Table('teamgame',
    # #                     db.Column("game_id", db.ForeignKey('game.id'), primary_key=True),
    # #                     db.Column("team_id", db.ForeignKey('team.id'), primary_key=True))
    

    # class Game(db.Model):
    #     id = db.Column(db.Integer, primary_key=True, unique=True)
    #     name = db.Column(db.String(10), nullable=False, unique=True)
    #     teams = db.relationship('Game', secondary=TeamGame, backref=db.backref('game', lazy=True))

    # class Team(db.Model):
    #     id = db.Column(db.Integer, primary_key=True, unique=True)
    #     name = db.Column(db.String(3), nullable=False, unique=True)
    #     games = db.relationship('Game', secondary=TeamGame, backref=db.backref('team', lazy=True))




    game_teams = db.Table(
        'game_teams',
        db.Column('game_id', db.Integer, db.ForeignKey('game.id'), primary_key=True),
        db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True, collection_class=MutableList)
    )

    class Game(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        teams = db.relationship('Team', secondary=game_teams, backref='games')

    class Team(db.Model):
        id = db.Column(db.Integer, primary_key=True)


    models = {}
    models['Game'] = Game
    models['Team'] = Team
    models['TeamGame'] = game_teams

    return models