import requests
from bs4 import BeautifulSoup

def url_fetcher():
    url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    try:
        response = requests.get(url)
        
        if response.status_code == 404:
            print("Page not found!")
            return None
        
        if response.status_code != 200:
            print(f"Error: Status code {response.status_code}")
            return None
            
        return response

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None

def check_price(response):
    if response is None:
        print("No response to parse.")
        return
        
    soup = BeautifulSoup(response.text, 'html.parser')

    product_box = soup.find('div', class_='col-sm-6 product_main')

    if product_box:
        title_tag = product_box.find("h1")
        price_tag = product_box.find("p", class_="price_color")
        
        if title_tag and price_tag:
            title = title_tag.text
            
            raw_price = price_tag.text
            cleaned_price_string = raw_price.replace("Â", "").replace("£","")
            
            price_float = float(cleaned_price_string)
            
            my_budget = 60.00
            
            print("-" * 50)
            print(f"📖 Book Title: {title}")
            print(f"💵 Current Price: £{price_float}")
            print("-" * 50)
            
            if price_float <= my_budget:
                print("🎉 GREAT NEWS! The price is within your budget. BUY NOW!")
            else:
                print("Too expensive! Wait for a price drop.")
        else:
            print("Could not find title or price inside the product block.")
    else:
        print("Could not find the product main container.")

server_response = url_fetcher()
check_price(server_response)