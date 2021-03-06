from YTAPI import YouTubeStats
from collections import defaultdict
import pytz
from datetime import datetime

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
            if "likeCount" not in item["statistics"]:
                rowResult[provide_dict[group_names[idx]][1][1]]=None
            else:
                rowResult[provide_dict[group_names[idx]][1][1]]=rowResult.get(provide_dict[group_names[idx]][1][1],item["statistics"]["likeCount"])
            valid_cols.extend([provide_dict[group_names[idx]][1][0],provide_dict[group_names[idx]][1][1]])
        
        valid_cols.append('update_time')
        tz_Seo = pytz.timezone('Asia/Seoul') 
        datetime_Seo = datetime.now(tz_Seo)
        fmt = '%Y-%m-%d %H:%M'
        rowResult['update_time']=datetime_Seo.strftime(fmt)

        self.db.insert_data(rowResult,valid_cols)

#performance_3_vocal
class Scraper_v():
    def __init__(self,db,api_key):
        self.db=db
        self.api_key=api_key
    def scrape(self,wjsnvivizID='',loonakep1erID='',hyolynbravegirlsID=''):
        provide_dict={
            'wjsnviviz':[wjsnvivizID,('wjsn_viviz_views','wjsn_viviz_likes')],
            'loonakep1er':[loonakep1erID,('loona_kep1er_views','loona_kep1er_likes')],
            'hyolynbravegirls':[hyolynbravegirlsID,('hyolyn_bravegirls_views','hyolyn_bravegirls_likes')],
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
            if "likeCount" not in item["statistics"]:
                rowResult[provide_dict[group_names[idx]][1][1]]=None
            else:
                rowResult[provide_dict[group_names[idx]][1][1]]=rowResult.get(provide_dict[group_names[idx]][1][1],item["statistics"]["likeCount"])
            valid_cols.extend([provide_dict[group_names[idx]][1][0],provide_dict[group_names[idx]][1][1]])
        
        valid_cols.append('update_time')
        tz_Seo = pytz.timezone('Asia/Seoul') 
        datetime_Seo = datetime.now(tz_Seo)
        fmt = '%Y-%m-%d %H:%M'
        rowResult['update_time']=datetime_Seo.strftime(fmt)

        self.db.insert_data(rowResult,valid_cols)

class Scraper_d():
    def __init__(self,db,api_key):
        self.db=db
        self.api_key=api_key
    def scrape(self,hoylynwjsnID='',bravegirlsloonaID='',viviz_kep1erID=''):
        provide_dict={
            'hoylynwjsn':[hoylynwjsnID,('hoylyn_wjsn_views','hoylyn_wjsn_likes')],
            'bravegirlsloona':[bravegirlsloonaID,('bravegirls_loona_views','bravegirls_loona_likes')],
            'viviz_kep1er':[viviz_kep1erID,('viviz_kep1er_views','viviz_kep1er_likes')],
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
            if "likeCount" not in item["statistics"]:
                rowResult[provide_dict[group_names[idx]][1][1]]=None
            else:
                rowResult[provide_dict[group_names[idx]][1][1]]=rowResult.get(provide_dict[group_names[idx]][1][1],item["statistics"]["likeCount"])
            valid_cols.extend([provide_dict[group_names[idx]][1][0],provide_dict[group_names[idx]][1][1]])
        
        valid_cols.append('update_time')
        tz_Seo = pytz.timezone('Asia/Seoul') 
        datetime_Seo = datetime.now(tz_Seo)
        fmt = '%Y-%m-%d %H:%M'
        rowResult['update_time']=datetime_Seo.strftime(fmt)

        self.db.insert_data(rowResult,valid_cols)

