import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'king god oss'

DATABASE_HOST = 'AWS RDS instance endpoint'
DATABASE_USERNAME = 'oss'
DATABASE_PASSWORD = 'AWS RDS instance password'
DEFAULT_DATABASE = 'imgtoss'

SQLALCHEMY_ECHO = True
SQLALCHEMY_BINDS = {
	DEFAULT_DATABASE: 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DEFAULT_DATABASE)
}
SQLALCHEMY_TRACK_MODIFICATIONS = True

AWS_ACCESS_KEY_ID = 'AWS Access Key Id'
AWS_SECRET_ACCESS_KEY = 'AWS Secret Access Key'
AWS_S3_BUCKET_NAME = 'imgtoss'