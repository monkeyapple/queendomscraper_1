from scraper import Scraper
from db import DatabaseOperations
import os

db=DatabaseOperations()
api_key=os.getenv('api_key')
scraper=Scraper(db,api_key)
scraper.scrape('txezJAgKX3w','DXtUAV5UsUw','','659vX2fuzcQ','9sycy5izQwY','')
