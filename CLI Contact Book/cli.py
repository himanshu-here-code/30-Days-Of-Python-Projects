contact_list ={}
while True:
    print("\n--- CONTACT BOOK MENU ---\n")
    print("1. Add A Contact")
    print("2. View All Contacts")
    print("3. Search A Contact")
    print("4. Delete A Contact")
    print("5. quit\n")
    user_choice = int(input("Please enter a number (1-5): "))
    if user_choice not in (1,2 ,3,4,5):
        print("Input invalid. Please enter a number from (1-5)")
        continue

    if user_choice == 1:
        name  = str(input("Please enter the name of contact holder: "))
        name = name.lower()
        contact = (input("Enter Your 10 digit Phone number: "))
        if len(contact) != 10 or not contact.isdigit():
            print("❌enter a valid 10 digits number.")
            continue
        if name in contact_list:
            print(f"Phone number is already registered on the name - {name}.")
            continue
        contact_list[name] = contact
        print(f"✅ Contact for {name} added successfully!")
    
    if user_choice == 2:
        print("ALL CONTACTS\n")
        for name in contact_list:
            print(f"{name} : {contact}")

    if user_choice == 3:
        user_search = input("search for user by his name: ")
        user_search = user_search.lower()
        if user_search not in contact_list:
            print("user in not in contact list")
        if user_search in contact_list:
            name = name.capitalize()
            print(f"{name} : {contact}")

    if user_choice ==4:
        del_user = input("name of the user: ")
        if del_user in contact_list:
            del_contact = input("Enter you contact number for verification: ")
            if del_contact in contact_list[del_user]:
                contact_list.pop(del_user)
                print(f"✅ Contact for {del_user} has been deleted.")
            else:
                print("❌ Verification failed. Number does not match.")
                
        else:
            print(f"❌ User '{del_user}' not found in contacts.")
               
    if user_choice ==5:
        print("GoodBye! have a great day.")
        break

