# $ pip install google-api-python-client
#

import keys
from googleapiclient.discovery import build


youtube = build('youtube', 'v3', developerKey=keys.YT_API_KEY)

# parameters for later use
keywords = ["weather", "temperature"]     # keyword I want to search
searchOrder = 'relevance'    # searches by date created. can also search by 'viewCount','relevance','title'(alphabetical),etc
numOfResults = 10       # number of results wanted

# making the request
request = youtube.search().list(
    part='snippet', q=keywords, maxResults=numOfResults, order=searchOrder
)

response = request.execute()['items']    # returns list of videos 
# print(response)

print("""
%2d most recent youtube video titles on "%s":
=======================================================""" %(numOfResults, keywords))
for i in range(numOfResults):
    title_vid1 = response[i]['snippet']['title']
    print("%2d. %s"%(i+1, title_vid1))

youtube.close()