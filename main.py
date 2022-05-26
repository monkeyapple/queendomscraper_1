from scraper import Scraper,Scraper_v,Scraper_d
from db import DatabaseOperations_1,DatabaseOperations_2, DatabaseOperations_3_v,DatabaseOperations_3_d,DatabaseOperations_3_final
import os
from dotenv import load_dotenv
load_dotenv()
#Initialize database opertion module
db_1=DatabaseOperations_1()
db_2=DatabaseOperations_2()
db_3_v=DatabaseOperations_3_v()
db_3_d=DatabaseOperations_3_d()
db_3=DatabaseOperations_3_final()

#Performance1
api_key_1=os.environ.get('api_key_1')
scraper_1=Scraper(db_1,api_key_1)
#wjsn,kep1er,viviz,hyolyn,loona,bravegirls
scraper_1.scrape(wjsnID='UITFHyWHS9Y',kep1erID='THiACt2pURE',vivizID='rY8Gz8bBoR8',hyolynID='2D2FoanXVL0',loonaID='87fKv045u5U',bravegirlsID='JfqGsj2FUBw')


#Performance2
api_key_2=os.environ.get('api_key_2')
scraper_2=Scraper(db_2,api_key_2)
#wjsn,kep1er,viviz,hyolyn,loona,bravegirl
scraper_2.scrape(wjsnID='9DBy1r7YMMg',kep1erID='EzJfJhznH3s',vivizID='NyjWRuazgsw',hyolynID='BEZk9QVjA-s',loonaID='ytuMObZlqOE',bravegirlsID='jjjg8kUcl20')


#Performance_3_vocal
api_key_3_v=os.environ.get('api_key_3_v')
scraper_3_v=Scraper_v(db_3_v,api_key_3_v)
#wjsn,kep1er,viviz,hyolyn,loona,bravegirls
scraper_3_v.scrape(wjsnvivizID='Wm1quwZiefQ',loonakep1erID='RkvoilXKGN4',hyolynbravegirlsID='qsCO_iifc30')

#Performance_3_dance
api_key_3_d=os.environ.get('api_key_3_d')
scraper_3_d=Scraper_d(db_3_d,api_key_3_d)
#wjsn,kep1er,viviz,hyolyn,loona,bravegirls
scraper_3_d.scrape(hoylynwjsnID='AthYcVXwBAY',bravegirlsloonaID='9nzIFQsUGVI',viviz_kep1erID='rKRowS7eo1I')

#Performance_3_final
api_key_3=os.environ.get('api_key_3')
scraper_3=Scraper(db_3,api_key_3)
#wjsn,kep1er,viviz,hyolyn,loona,bravegirl
scraper_3.scrape(wjsnID='hDm0qLxZd9I',kep1erID='B2xLS0GVeNI',vivizID='XxDKzs5pT1E',hyolynID='o6QFNoJS1Iw',loonaID='aXaHB4gGAys',bravegirlsID='MShOLenjduY')
