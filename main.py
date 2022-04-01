from scraper import Scraper
from db import DatabaseOperations
import os

db=DatabaseOperations()
api_key=os.environ.get('api_key')
scraper=Scraper(db,api_key)
#wjsn,kep1er,viviz,hyolyn,loona,bravegirls
scraper.scrape(wjsnID='',kep1erID='',vivizID='rY8Gz8bBoR8',hyolynID='2D2FoanXVL0',loonaID='',bravegirlsID='')