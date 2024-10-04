import requests

url = "https://twitter154.p.rapidapi.com/search/search"


headers = {
	"x-rapidapi-key": "3e2029feeamsh52efed887c13ab2p1c3cf4jsn40ead3bbef86",
	"x-rapidapi-host": "twitter154.p.rapidapi.com"
}

    

def call_search(query,min_retweets= 5000,limit=10,min_likes= 5000,start_date= "2024-01-01",language= "es" ):
    querystring = {
    "query": query,
    "section": "top",
    "min_retweets": min_retweets,
    "limit": limit,
    "min_likes": min_likes,
    "start_date": start_date,
    "language": language}
    

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

