import os
import databases
from dotenv import load_dotenv

load_dotenv()

TEST_DATABASE_URL = os.environ.get('POSTGRES_TEST')