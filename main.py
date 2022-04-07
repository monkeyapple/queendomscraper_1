from scraper import Scraper
from db import DatabaseOperations
import os

db=DatabaseOperations()
api_key=os.environ.get('api_key')
scraper=Scraper(db,api_key)
#wjsn,kep1er,viviz,hyolyn,loona,bravegirls
scraper.scrape(wjsnID='UITFHyWHS9Y',kep1erID='THiACt2pURE',vivizID='rY8Gz8bBoR8',hyolynID='2D2FoanXVL0',loonaID='87fKv045u5U',bravegirlsID='JfqGsj2FUBw')