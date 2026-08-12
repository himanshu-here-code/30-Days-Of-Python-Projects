import requests

def urlfetcher():
    url = "https://v2.jokeapi.dev/joke/Any"
    try:
        response = requests.get(url)
        if response.status_code == 404:
            print(f"Page not found!")
            return None
        
        if response.status_code != 200:
            print(f"Page not found. Error {response.status_code}")
            return None
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None  

def joke(joke_data):
    if joke_data is None:
        print("No response")
        return

    category = joke_data.get('category', 'Unknown')
    joke_type = joke_data.get('type', 'unknown')
    
    print("-" * 40)
    print(f"Category: {category}")
    print(f"Type: {joke_type}")

    if joke_type == "twopart":
        setup = joke_data.get('setup', 'No setup available')
        delivery = joke_data.get('delivery', 'No delivery available')
        print(f"JOKE SETUP: {setup}")
        print(f"JOKE DELIVERY: {delivery}")
    else:
        joke = joke_data.get('joke', 'No joke available')
        print(f"JOKE: {joke}")
    
    print("-" * 40)

joke_data = urlfetcher()
joke(joke_data)

while True:
    user_choice = input("Do YOU want more? (y/n): ")
    if user_choice == "y":
        joke_data = urlfetcher()
        joke(joke_data)
    else:
        break