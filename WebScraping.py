#Will need to grab the request library
from bs4 import BeautifulSoup
import requests
import json

#GET Request
req = requests.get('http://quotes.toscrape.com')
soup = BeautifulSoup(req.text, "html.parser")


quote = soup.findAll("span", attrs={"class":"text"})
author = soup.findAll("small", attrs={"class":"author"})

#For Loop To Gather the Quote and the Author of the Quote
for quote in quote:
    print(quote.text)
for author in author:
    print(author.text)

#Input
continueProgram = input("Pause Break. Type anything to see the rest of the results in html ")

#Gathers HTML Code
print(req)
print(req.content)

# Open File. With statement automatically closes it 
with open("bioInfo.json", "r") as infoFile:
    data = json.load(infoFile)

# Use dump function to encode the JSON file
    with open("bioInfoResults.json", "w") as infoFile:
        json.dump(data, infoFile)
