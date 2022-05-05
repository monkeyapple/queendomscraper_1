from scraper import Scraper,Scraper_v
from db import DatabaseOperations_1,DatabaseOperations_2, DatabaseOperations_3_v
import os
from dotenv import load_dotenv
load_dotenv()
#Initialize database opertion module
db_1=DatabaseOperations_1()
db_2=DatabaseOperations_2()
db_3_v=DatabaseOperations_3_v()

#Performance1
api_key_1=os.environ.get('api_key_1')
scraper_1=Scraper(db_1,api_key_1)
#wjsn,kep1er,viviz,hyolyn,loona,bravegirls
scraper_1.scrape(wjsnID='UITFHyWHS9Y',kep1erID='THiACt2pURE',vivizID='rY8Gz8bBoR8',hyolynID='2D2FoanXVL0',loonaID='87fKv045u5U',bravegirlsID='JfqGsj2FUBw')


#Performance2
api_key_2=os.environ.get('api_key_2')
scraper_2=Scraper(db_2,api_key_2)
#wjsn,kep1er,viviz,hyolyn,loona,bravegirls
scraper_2.scrape(wjsnID='9DBy1r7YMMg',kep1erID='EzJfJhznH3s',vivizID='NyjWRuazgsw',hyolynID='BEZk9QVjA-s',loonaID='ytuMObZlqOE',bravegirlsID='jjjg8kUcl20')


#Performance_3_vocal
api_key_3_v=os.environ.get('api_key_3_v')
scraper_3_v=Scraper_v(db_3_v,api_key_3_v)
#wjsn,kep1er,viviz,hyolyn,loona,bravegirls
scraper_3_v.scrape(wjsnvivizID='Wm1quwZiefQ',loonakep1erID='RkvoilXKGN4',hyolynbravegirlsID='qsCO_iifc30')

