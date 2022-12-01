from flaskblog import db

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    json = db.Column(db.JSON, nullable=True)

    def __repr__(self):
        return f"Report: {self.json}"