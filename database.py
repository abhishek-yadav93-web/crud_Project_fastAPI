from config import root,pwd,db_name
import crud_Project.config as config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
 
root =config.root      
pwd = config.pwd     
db_name = config.db_name  
 
SQLALCHEMY_DATABASE_URL =f'mysql+pymysql://{root}:{quote_plus(pwd)}@localhost/{db_name}'
 
engine = create_engine(SQLALCHEMY_DATABASE_URL)
 
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
 
Base = declarative_base()
 
