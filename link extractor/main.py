from bs4 import BeautifulSoup
import requests


url = input("Enter the url: ")

# fetching html page
response = requests.get(url)

document = response.text

soup = BeautifulSoup(document, "html.parser")

with open("./output.txt", "w") as file:
    file.truncate(0)
    for links in soup.find_all("a"):
        file.write(str(links.get("href"))+"\n\n")


print("Successfully extracted all links checkout output.txt")
