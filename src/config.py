import os

from dotenv import load_dotenv
env_vars_to_clear = ['DB_NAME', 'DB_USER', 'DB_PASS', 'DB_HOST', 'DB_PORT', 'SECRET_AUTH', 'SMTP_USER', 'SMTP_PASSWORD', 'SMTP_HOST', 'SMTP_PORT', 'MODE']

for var in env_vars_to_clear:
    os.environ.pop(var, None)

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
SECRET_AUTH = os.environ.get("SECRET_AUTH")

DB_TEST_HOST = os.environ.get("DB_TEST_HOST")
DB_TEST_PORT = os.environ.get("DB_TEST_PORT")
DB_TEST_NAME = os.environ.get("DB_TEST_NAME")
DB_TEST_USER = os.environ.get("DB_TEST_USER")
DB_TEST_PASS = os.environ.get("DB_TEST_PASS")
SECRET_TEST_AUTH = os.environ.get("SECRET_TEST_AUTH")
