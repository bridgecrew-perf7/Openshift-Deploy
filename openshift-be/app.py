import os

from flask import Flask, Blueprint
from flask_restx import Api
from openshift_be.configs.database import db
from openshift_be.configs.ma import ma
from openshift_be.configs.config import SQLALCHEMY_TRACK_MODIFICATIONS
from decouple import config
from openshift_be.routes.modelRoutes import name_ns, Name
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    ma.init_app(app)
    CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
    blueprint = Blueprint('api', __name__, url_prefix='/api/v1/')
    api = Api(blueprint, title="Sample Flask_Restx App")
    app.register_blueprint(blueprint)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

    api.add_namespace(name_ns)

    name_ns.add_resource(Name, "")

    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    create_app.run(host='0.0.0.0', debug=True)