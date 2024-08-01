from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Create an SQLite database
engine = create_engine('sqlite:///rps_game.db', echo=False)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)
