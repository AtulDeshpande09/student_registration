import os

class Config:
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://atul:atul@localhost/student_db'
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = os.urandom(24)
    

