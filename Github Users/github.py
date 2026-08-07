import requests
import json
import os

def save_to_json(username, user_data):
    folder = "Github Users/github_user_data.json"
    if os.path.exists(folder):
        with open(folder ,"r") as f:
            all_users = json.load(f)
    else:
        all_users = {}
    
    all_users[username] = {
        "name" : user_data.get("name","not provided"),
        "bio" : user_data.get("bio" , "not provided"),
        "public_repos" : user_data.get("public_repos", 0),
        "followers" : user_data.get("followers", 0)
    }

    with open(folder ,"w") as f:
        json.dump(all_users, f  , indent=4)
        print("USER DETAILS SAVED")


def get_user(username):
    url = f"https://api.github.com/users/{username}" 
    try:
        response = requests.get(url)
        if response.status_code == 404:
            print(f"{username} not found!")
            return None
        
        if response.status_code != 200:
            print(f"user not found. error {response.status_code}")
            return None
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def github_user(user_data):
    if not user_data:
        return
    name = user_data.get("name","not provided")
    bio = user_data.get("bio" , "not provided")
    public_repos = user_data.get("public_repos", 0)
    followers = user_data.get("followers", 0)
    
    print(f"Name: {name}")
    print(f"Bio: {bio}")
    print(f"Public Repositories: {public_repos}")
    print(f"Followers: {followers}")
    
    
def interactive():
    username = input("Enter Github username: ")
    user_data = get_user(username)
    if user_data:
        github_user(user_data)
        save_choice = input("Do you want to save this profile? (y/n): ")
        if save_choice.lower() == 'y':
            save_to_json(username, user_data)

if __name__ == "__main__":
   interactive()