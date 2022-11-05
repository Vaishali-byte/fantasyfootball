# How your databases are going to look. 
from application import db 

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    position = db.Column(db.String(60))
    fk_teamid = db.Column(db.Integer, db.ForeignKey('teams.id'))