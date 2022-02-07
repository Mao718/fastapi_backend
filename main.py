from configs.database import SessionLocal, engine
from API.apis import app
from loader import loader
#import models.users as models
# models.Base.metadata.create_all(bind=engine)  # bulit db with the models file

# define app  #loader
