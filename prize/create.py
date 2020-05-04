 
from application import db
from application.models import Users, Prizes
db.drop_all()
db.create_all()