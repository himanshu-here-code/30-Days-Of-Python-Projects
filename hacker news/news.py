import requests
from bs4 import BeautifulSoup

def url_fetcher():
    url = "https://news.ycombinator.com/"
    try:
        response = requests.get(url)
        if response.status_code == 404:
            print(f"Page not found!")
            return None
        
        if response.status_code != 200:
            print(f"Page not found. Error {response.status_code}")
            return None
        
        return response
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None  
    
def news(response):

    if response is None:
        print("No response to parse")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('span', class_='titleline')

    for article in articles:
        link_tag = article.find("a")
        if link_tag:
            title = link_tag.text
            url1 = link_tag.get("href")  
            print(f"Title : {title}")
            print(f"Url : {url1}")
            print("-" * 50)
        else:
            print("No link found in this article")

response = url_fetcher()
news(response)