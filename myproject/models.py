from myproject import db

class Car(db.Model):

    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='car', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Car name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Car name is {self.name} and has no owner assigned yet."

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))

    def __init__(self, name, car_id):
        self.name = name
        self.car_id = car_id

    def __repr__(self):
        return f"Owner Name: {self.name}"