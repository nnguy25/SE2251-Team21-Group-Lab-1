# keys for use
import keys

# ===========GEOCODE===========
import requests, json, datetime
we_api_key = keys.WEA_API_KEY

def getCoords(location):
    geocode_url = "http://api.openweathermap.org/geo/1.0/direct?q="
    complete_gc_url = geocode_url + location +"&appid=" + we_api_key

    responseGeo = requests.get(complete_gc_url)
    return responseGeo.json()



# getting coords with location
location=input("What location: ")
coordinates = getCoords(location)
# latitude and longitude for later use
lat = coordinates[0]["lat"]
lon = coordinates[0]["lon"]
# ===========GEOCODE===========




# ===========OPENWEATHER===========
class OpenWeatherAPI:
    def __init__(self):
        # max_temp = 0
        # min_temp = 0
        curr_temp = 0       # kelvins
        curr_pressure = 0   # hPa unit
        curr_hummidity = 0  # %
        weather_desc = ''

    @classmethod
    def fillInfo(self,lat,lon):
        # url info
        complete_url = "http://api.openweathermap.org/data/2.5/weather?lat="+str(lat) +"&lon="+str(lon)+ "&appid=" + we_api_key
        
        responseOW = requests.get(complete_url)
        general_weather_info = responseOW.json()
        
        # store the value of "main" key in variable air_c
        air_conditions = general_weather_info["main"]
        # store various value corresponding to the respective keys of air_c
        self.curr_temp = air_conditions["temp"]
        self.curr_pressure = air_conditions["pressure"]
        self.curr_humidity = air_conditions["humidity"]
    
        # store description of "weather" key
        self.weather_desc = general_weather_info["weather"][0]["description"]
        

london_weather = OpenWeatherAPI
london_weather.fillInfo(lat,lon) # can now get weather info by london_weather.<attribute>
# ===========OPENWEATHER===========




# ===========YOUTUBE===========
from googleapiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=keys.YT_API_KEY)

class YoutubeAPI:

    def __init__(self, searchOrder='relevence'):
        self.searchOrder = searchOrder
        self.videoList = []


    @classmethod
    def fillVideoList(self, lat, lon, keywords):
        # making the request
        request_vid = youtube.search().list(
            part='snippet', location=("%s,%s"%(str(lat),str(lon))), locationRadius='10mi',q=keywords, maxResults=numOfResults, order=searchOrder, type='video'
        )
        response_vid = request_vid.execute()['items']    # populates with list of videos
        self.videoList = response_vid

    @classmethod
    def videoAndChannelInfo(self, videoNumber):
        vidID = self.videoList[videoNumber]['id']['videoId']
        ch_id = self.videoList[videoNumber]['snippet']['channelId']

        request_ch = youtube.channels().list(
            part='snippet', id=ch_id
        )
        ch_info = request_ch.execute()['items'][0]

        vid_title = self.videoList[videoNumber]['snippet']['title']
        ch_title = ch_info['snippet']['title']

        return {'title':vid_title,'channel':ch_title}
        

# parameters for later use
keywords = ["weather", "temperature"]     # keyword I want to search
searchOrder = 'relevance'    # searches by date created. can also search by 'viewCount','relevance','title'(alphabetical),etc
numOfResults = 5       # number of results wanted

london_videos = YoutubeAPI
london_videos.fillVideoList(lat, lon, keywords)
video2 = london_videos.videoAndChannelInfo(2)

print(video2)
# youtube.close()
# ===========YOUTUBE===========



# ===========TWITTER===========
# code
# ===========TWITTER===========