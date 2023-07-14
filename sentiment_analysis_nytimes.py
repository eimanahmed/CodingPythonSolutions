#The goal of this code is to take a set of search_keywords that the user provides
#and determine the total number of articles that the NY Times has written on this topic
#as well as determine whether the NYTimes reports information using a positive or negative tone
#and whether the NY Times uses an objective format or subjective format of speech

#Import modules to be used in analysis
import requests, textblob

#The API_KEY must be replaced with the person's API
#The url is the endpoint that a request is being made to
#Here, the request is to the Article Search API to get articles and their 
#relevant information back
url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
API_KEY = ""

#Specifying the query using the user's input
#API_KEY remains the same, query is provided with the information the user stated
search_keywords = input("What articles are you interested in analyzing? ")
params = {"query": search_keywords, "api-key": API_KEY}

#Performing a get request to retrieve information from the API
#After, I am retrieving the total number of articles on a topic by looking 
#into the response dictionary I get back from the Article Search API
response = requests.get(url, params)
num_articles = response.json()['response']['meta']['hits']

print(f"There are {num_articles:,} about {search_keywords} published in the NY Times")

#Creating an iteratable object so I can use a loop to go through the abstracts 
#of articles one by one and determine whether they are positive, negative,
#subjective or objective
iter_docs = response.json()['response']['docs']

#Creating a dictionary to hold my relevant information
#You can use variables too but a dictionary is more efficient 
sentiment = {'positive':0, 'negative': 0, 'subjective': 0, 'objective': 0}

#Iterating over the abstracts of the articles from the search performed
#Then, counting whether each article is negative, positive, subjective, or objective
#by incrementing the values of my relevant dictionary keys by 1

#The logic being used to determine negative, positive, subjective, objective is based
#on the Textblob website. 
#Polarity ranges from -1 to 1 with -1 being very negative, 0 as neutral, +1 as very positive
#Subjectivity ranges from 0 to 1 with 0 being very objective, 0.5 being neither, 1 being very subjective
for each_doc in iter_docs:
    abstract_sentiment = textblob.TextBlob(each_doc['abstract']).sentiment
    if abstract_sentiment[0] < 0:
        sentiment['negative'] += 1
    else:
        sentiment['positive'] += 1
    if abstract_sentiment[1] <= 0.5:
        sentiment['objective'] += 1
    else:
        sentiment['subjective'] += 1

#Using conditional comparisons to determine whether the NY Times reports more 
#positive toned articles than negative, about the same amount, or less than
if sentiment['positive'] == sentiment['negative']:
    print("The New York Times usually has a neutral tone in articles")
elif sentiment['positive'] < sentiment['negative']:
    print("The New York Times usually has a positive tone in articles")
else:
    print("The New York Times usually has a negative tone in articles")

#Using conditional comparisons to determine whether the NY Times reports more 
#objective toned articles than subjective, about the same amount, or less than
if sentiment['subjective'] == sentiment['objective']:
    print("The New York Times is neither subjective, nor objective")
elif sentiment['subjective'] < sentiment['objective']:
    print("The New York Times is usually subjective")
else:
    print("The New York Times is usually objective")

