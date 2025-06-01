sgrocery =input("enter your grocer_list(using commas)")
grocery=[sgrocery]
while True:
    print("\nOptions:add / remove / show /exit")
    action=input("what would you like to do? ")
    if action =="add":
        item=input("Enter item  to add: ")
        grocery.append(item)
        print(f"{item}added")
        
    elif action =="remove":
        item = input("Enter item to remove: ")
        if item in grocery:
            grocery.remove(item)
            print(f"{item}removed.")
        else:
            print("item not found.")

    elif action =="show":
        print("your grocery list:")
        for i in grocery:
            print("-",i)

    elif action =="exit":
        break
    else:
        print("invalid options.")