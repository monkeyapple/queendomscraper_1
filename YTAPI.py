import requests
import json
class YouTubeStats():
    def __init__(self,api_key,video_ids):
       
        self.api_key=api_key
        self.video_ids=video_ids
    def getUrlResponse(self,url):
        i = 0
        while i < 3:
            try:
                res = requests.get(url, timeout=5)
                return res
            except (requests.exceptions.ChunkedEncodingError, requests.ConnectionError) as e:
                print("There is a error: %s" % e)
                i += 1
    def get_video_stats(self):
        url=f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={self.video_ids}&key={self.api_key}'
        response=self.getUrlResponse(url)
        data=json.loads(response.text)
        return data["items"]



            
