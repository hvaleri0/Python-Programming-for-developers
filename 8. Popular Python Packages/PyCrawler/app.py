import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")

# specify the type of parser eg. html.parser:
soup = BeautifulSoup(response.text, "html.parser")

# specify the class you want to scrape eg. class="question-summary":
questions = soup.select(".question-summary")
print(questions[0].attrs)

# best practice in case id attibute is missin defaults to 0:
print(questions[0].get("id", 0))

# dig in deeper to get the questions:
print(questions[0].select(".question-hyperlink"))

# when dealing with a single element use select_one
print(questions[0].select_one(".question-hyperlink"))

# use getText method to extract the text
print(questions[0].select_one(".question-hyperlink").getText())

# now we iterate!
for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())
