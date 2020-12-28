import logging
from app.ext.db import engine
from . import user

logging.getLogger().setLevel('INFO')


# Generate all models
def generate_models():
    logging.info('Creating database models...')
    user.Base.metadata.create_all(bind=engine)
    logging.info('Database models created')