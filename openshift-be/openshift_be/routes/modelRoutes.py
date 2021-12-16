from flask_restx import Resource, Namespace, fields
from flask import request, jsonify
from sqlalchemy import desc
from openshift_be.configs.database import db

from openshift_be.models.models import Names
from openshift_be.schemas.modelschema import NamesSchema

name_ns = Namespace('names', description="Names API")

name_schema = NamesSchema()
names_schema = NamesSchema(many=True)

name = name_ns.model('Names', {
    'submittedName': fields.String('first name')
})

class Name(Resource):
    @name_ns.doc('get recent name')
    def get(self):
        get_name = db.session.query(Names).order_by(Names.id.desc()).first()
        return name_schema.dump(get_name), 200

    @name_ns.expect(name)
    @name_ns.doc('Enter name')
    def post(self):
        name_json = request.get_json()
        newName = Names(fName=name_json['submittedName'])
        db.session.add(newName)
        db.session.commit()
        return name_schema.dump(newName), 200