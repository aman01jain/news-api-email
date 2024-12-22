import requests
from send_email import email_send

topic = "tesla"
api_key = "95ee796b231b44a0b9e7c7e62a373926"
url= f"https://newsapi.org/v2/everything?q={topic}&" \
     "from=2024-11-22&sortBy=publishedAt&apiKey=" \
     "95ee796b231b44a0b9e7c7e62a373926&" \
     "language=en"

request = requests.get(url)
content = request.json()

# Access the article title and description
body = " "
for article in content["articles"][0:10]:
    if article["title"] is not None:
        body = "Subject: Today's news" \
               + "\n" +body +article["title"] + "\n" \
               + article["description"] +"\n" +\
               article["url"] + 2*"\n"

    body = body.encode("utf-8")
    email_send(message=body)
