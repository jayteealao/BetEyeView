from dotenv import load_dotenv
import os
import databases
import sqlalchemy

load_dotenv()


DATABASE_URL = os.environ.get('POSTGRES', None)

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
