from YTAPI import YouTubeStats
from collections import defaultdict
import pytz
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

class Scraper():
    def __init__(self,db,api_key):
        self.db=db
        self.api_key=api_key
    def scrape(self,wjsnID='',kep1erID='',vivizID='',hyolynID='',loonaID='',bravegirlsID=''):
        provide_dict={
            'wjsn':[wjsnID,('wjsn_views','wjsn_likes')],
            'kep1er':[kep1erID,('kep1er_views','kep1er_likes')],
            'viviz':[vivizID,('viviz_views','viviz_likes')],
            'hyolyn':[hyolynID,('hyolyn_views','hyolyn_likes')],
            'loona':[loonaID,('loona_views','loona_likes')],
            'bravegirls':[bravegirlsID,('bravegirls_views','bravegirls_likes')]
            }

        video_dict=defaultdict(str)
        for i in provide_dict:
            if provide_dict[i][0]!='':
                video_dict[i]=provide_dict[i][0]
        video_ids=",".join(video_dict.values())
        group_names=list(video_dict.keys())

        ytstats=YouTubeStats(self.api_key,video_ids)
        items=ytstats.get_video_stats()

        rowResult={}
        valid_cols=[]
        for idx,item in enumerate(items):
            rowResult[provide_dict[group_names[idx]][1][0]]=rowResult.get(provide_dict[group_names[idx]][1][0],item["statistics"]["viewCount"])
            rowResult[provide_dict[group_names[idx]][1][1]]=rowResult.get(provide_dict[group_names[idx]][1][1],item["statistics"]["likeCount"])
            valid_cols.extend([provide_dict[group_names[idx]][1][0],provide_dict[group_names[idx]][1][1]])
        valid_cols.append('update_time')
        tz_Seo = pytz.timezone('Asia/Seoul') 
        datetime_Seo = datetime.now(tz_Seo)
        fmt = '%Y-%m-%d %H:%M'
        rowResult['update_time']=datetime_Seo.strftime(fmt)

        self.db.insert_data(rowResult,valid_cols)


