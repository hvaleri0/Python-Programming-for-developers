import requests  # pacakage for http requesting
import config

url = "https://api.yelp.com/v3/businesses/search"
api_key = "CrwtMxNTFapoHrw2H3afPt9wV3b-VF8Gca_xfFY1E2tEMpQ00QqOhL4R461xUGEFerKV57DrImHtYIfMpqVh7L5IsRWbn-yrqx6xS6iFISEFyuX1D-cnIdjIl3pSYHYx"
headers = {
    "Authorization": "Bearer "+config.api_key
}
params = {
    "term": "barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
# print(response.text)  # use .text to identify any error or results
businesses = response.json()['businesses']  # to convert to a dictionary
# Now we can iterate:
for business in businesses:
    print(business["name"])

# next level get business greater then 4.5 rating
names = [business["name"]
         for business in businesses if business["rating"] > 4.5]
print(names)
