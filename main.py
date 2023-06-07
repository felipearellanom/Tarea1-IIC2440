import csv


with open("tweets_2022_abril_junio.csv", "r", encoding="utf-8") as file:
  tweets = csv.DictReader(file)
  for tweet in tweets:
    
    print(tweet["text"])
    if tweet["id"] == "1512186831277895684":
      break