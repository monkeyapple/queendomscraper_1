from scraper import Scraper
from db import DatabaseOperations
import os

db=DatabaseOperations()
api_key=os.environ.get('api_key')
scraper=Scraper(db,api_key)
scraper.scrape('','','rY8Gz8bBoR8','2D2FoanXVL0','','')