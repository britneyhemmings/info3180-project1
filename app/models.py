from . import db


class PropertyInfo(db.Model):
    
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    rooms = db.Column(db.String(80))
    bathrooms = db.Column(db.String(80))
    price = db.Column(db.String(100))
    location = db.Column(db.String(400))
    pType = db.Column(db.String(80))
    image = db.Column(db.String(255)) #filename

    def __init__(self,title,description,rooms,bathrooms,price,pType,location, image):
        self.title = title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.pType = pType
        self.location = location
        self.image = image
        

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<PropertyInfo %r>' % (self.title)