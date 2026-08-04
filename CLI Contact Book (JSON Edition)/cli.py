import json
import os

folder = "CLI Contact Book (JSON Edition)/users.json"
if os.path.exists(folder):
    with open(folder, "r") as file:
        contacts = json.load(file)
else:
    contacts ={}

while True:
    print("\n--- CONTACT BOOK MENU ---\n")
    print("1. Add A Contact")
    print("2. View All Contacts")
    print("3. Search A Contact")
    print("4. Delete A Contact")
    print("5. quit\n")
    try:
        user_choice = int(input("Please enter a number (1-5): "))
        if user_choice not in (1, 2, 3, 4, 5):
            continue
    except ValueError:
        print("❌Please Enter a valid number")
        
    try:
        if user_choice == 1:

            name = str(input("Please enter the name of contact holder: "))
            name = name.lower()
            if name in contacts:
                print(f"there is already a contact on this name.\ntry another name or write your name differently \nfor example :({name}123)")
                continue
            contact = input("Enter Your 10 digit Phone number: ")
    
            if len(contact) != 10 or not contact.isdigit():
                print("❌ enter a valid 10 digits number.")
                continue
            
            if contact in contacts.values():
                print("contact number already taken")
                continue

            contacts[name] = contact
            with open(folder, "w") as file:
                json.dump(contacts, file, indent=4)
                print(f"✅ Contact for {name} added successfully!")

        if user_choice ==2:
            print("\nAll Contacts\n")
            for user_name, user_contacts in contacts.items():
                print(f"{user_name.capitalize()} : {user_contacts}")

        if user_choice == 3:
            print("--SEARCH USER--")
            search_user = input("Enter user name: ")
            search_user = search_user.lower()
            if search_user in contacts:
                print(f"{search_user.capitalize()} : {contacts[search_user]}")
            else:
                print("User not found. please check name.")

            enquiry = str(input("was the search accurate? (y/n): "))
            enquiry = enquiry.lower()
            if len(enquiry) != 1:
                print(len(enquiry))
            if enquiry == "y":
                    print("thx for feedback.")
            if enquiry == "n":
                    print("thx for feedback.")
        
        if user_choice == 4:
            print("---DELETE CONATCT---")
            del_user = input("Enter your name: ")
            del_user = del_user.lower()
            if del_user not in contacts:
                print(f"user not found. Check name again.")

            if del_user in contacts:
                del_contact = input("Enter your Contact number: ")
                if del_contact in contacts[del_user]:
                    contacts.pop(del_user)
                    with open(folder , "w") as file:
                        json.dump(contacts ,file ,indent=4)
                        print(f"Contact for {del_user.capitalize()} is deleted.")
                else:
                    print("Your contact number is wrong.Try again.")
        
        if user_choice == 5:
            print("GoodBye!")
            break
    except NameError:
        continue