from scraper import Scraper
from db import DatabaseOperations_1,DatabaseOperations_2
import os
from dotenv import load_dotenv
load_dotenv()
#Initialize database opertion module
db_1=DatabaseOperations_1()
db_2=DatabaseOperations_2()

#Performance1
api_key_1=os.environ.get('api_key_1')
scraper_1=Scraper(db_1,api_key_1)
#wjsn,kep1er,viviz,hyolyn,loona,bravegirls
scraper_1.scrape(wjsnID='UITFHyWHS9Y',kep1erID='THiACt2pURE',vivizID='rY8Gz8bBoR8',hyolynID='2D2FoanXVL0',loonaID='87fKv045u5U',bravegirlsID='JfqGsj2FUBw')


#Performance2
api_key_2=os.environ.get('api_key_2')
scraper_2=Scraper(db_2,api_key_2)
#wjsn,kep1er,viviz,hyolyn,loona,bravegirls
scraper_2.scrape(wjsnID='9DBy1r7YMMg',kep1erID='',vivizID='',hyolynID='',loonaID='ytuMObZlqOE',bravegirlsID='jjjg8kUcl20')