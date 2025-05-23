from fastapi import FastAPI
import requests # This allows us to get data from the internet
from bs4 import BeautifulSoup # This allows us to parse HTML 
from lxml import etree # This allows easily extracting data from HTML


app = FastAPI()


@app.get("/ethereum")
def ethereum():
    url = "https://coinmarketcap.com/"
    response = requests.get(url) # Get the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser") # Parse the HTML content with BeautifulSoup
    dom = etree.HTML(str(soup)) # Convert the BeautifulSoup object to an lxml object for easier XPath queries
    # The ethereum price as a XPATH
    price = dom.xpath('//*[@id="__next"]/div[2]/div[1]/div[2]/div/div[1]/div[5]/div/table/tbody/tr[2]/td[4]/div/span')[0].text
    print("The price of Ethereum is: " + price, "USD.") # Print the price of Bitcoin

    return {"Ethereum Price": price}