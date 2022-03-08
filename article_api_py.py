#TAKE OUT API CODE BEFORE LOADING TO GITHUB

#using NewsAPI to get new data for encrypting

import requests
from newsapi import NewsApiClient

#Initilize API
newsapi = NewsApiClient(api_key = 'de5151d82dfa46008dad2a320afefc4f')

#Function that pulls the top story from BBC News
def BBCNews():
    query_params = {
        'source': 'bbc-news',
        'sortBy': 'top',
        'apiKey': "de5151d82dfa46008dad2a320afefc4f"
    }
    url = 'https://newsapi.org/v1/articles'
    
    #fetch data and return in JSON format
    request = requests.get(url, params=query_params)
    open_page = request.json()
    
    #get articles as strings
    article = open_page['articles']
    
    #create a list that will store the news results
    news_results = []
    
    #loop to append to results
    for i in article:
        news_results.append(i['title'])
        
    for j in range(len(news_results)):
        print(j + 1, news_results[j])
    
    #Write the output to a txt file to be used in encryption 
    with open("BBC.txt", 'w') as file:
        for row in news_results:
            s = " ".join(map(str, row))
            file.write(s+'\n')

# Driver Code
if __name__ == '__main__':
    BBCNews()