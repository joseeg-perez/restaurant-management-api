from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv
from pathlib import Path
import os

Base = declarative_base()

env_path = Path('/src') / '.env'
load_dotenv(dotenv_path=env_path)

engine = create_engine(os.environ['DB'])
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)