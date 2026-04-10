from app.extensions import db   # ✅ FIX THIS

class Task(db.Model):
    __tablename__ = "task"


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='Pending')
    
