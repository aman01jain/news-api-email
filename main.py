import requests

api_key = "95ee796b231b44a0b9e7c7e62a373926"
url= "https://newsapi.org/v2/everything?q=tesla&" \
     "from=2024-11-22&sortBy=publishedAt&apiKey=" \
     "95ee796b231b44a0b9e7c7e62a373926"

request = requests.get(url)
content = request.json()

# Access the article title and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
