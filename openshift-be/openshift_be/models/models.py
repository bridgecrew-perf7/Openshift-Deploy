from openshift_be.configs.database import db

class Names(db.Model):
    __tablename__ = 'names'

    id = db.Column(db.Integer, primary_key=True)
    fName = db.Column(db.String())