from sqlalchemy.ext.declarative import declarative_base

from project.environment import env

Base = declarative_base()

settings = {
    'TEMPLATES': {
        'DIRS': ['templates'],
    },
    'DATABASE': {
        'URL': env['DATABASE_URL'],
        'METADATA': Base.metadata
    },
    'ATTEMPTS': env['ATTEMPTS'],
}
