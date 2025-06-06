#Add items one after the other to ensure smooth sales
grocery=[]

while True:
    print("\nOptions:add / remove / show /exit")
    action=input("what would you like to do? ").strip() .lower()

    if action =="add":
       print("\n#add items one after the other to ensure smooth sales")
       item=input("Enter item  to add: ")
       grocery.append(item)
       print(f"{item} added")
        
    elif action =="remove":
        item = input("Enter item to remove: ").strip()
        if item in grocery:
            grocery.remove(item)
            print(f"{item} removed.")
        else:
            print("item not found.")

    elif action =="show":
        print("\nYour grocery list:")
        if grocery:
           for i in grocery:
              print("-", i)
        else:
               print("Your list is empty.")

    elif action =="exit":
        print("Goodbye! Thanks for using the grocery app.")
        break

    else:
        print("invalid options.Please choose:add,remove,show, or exit.")