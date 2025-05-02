from flask import current_app
from apps import db

# Use the SQLAlchemy session to query users
users = db.session.execute("SELECT * FROM users").fetchall()
print(users)