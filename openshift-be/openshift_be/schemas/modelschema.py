from openshift_be.configs.ma import ma
from openshift_be.models.models import *

class NamesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Names
        load_instance=True