from dotenv import dotenv_values

import databases
import sqlalchemy

config = dotenv_values('.env')

DATABASE_URL = config['POSTGRES']
database = databases.Database(DATABASE_URL, force_rollback=True)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)