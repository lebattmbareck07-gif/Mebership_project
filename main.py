from utils import *
try:
  with open("Basket.json", "r") as file:
        lista=json.load(file)  
except FileNotFoundError:
    lista=[]
except json.JSONDecodeError:
    lista=[]
while True:
    clear_screen()
    print("\n** Welcome to gym Membership Management **\n")
    print("Choose an Action\n")
    print("1. Add new Member\n2. Display all Members\n3. Search for a Member\n4. Edit Member\n5. Delete Member\n6. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        lista.append(create_user(lista).to_dict())
        save_member(lista)
        print("Member added successfuly!")
        time.sleep(2)
    elif choice=="2": 
        if len(lista)>0:
            displaying_member(lista) 
        else:
            print("No members to display, Try to add one!!!")
            time.sleep(2)
    elif choice=="3":
        if lista:
            search_member(lista)
        else:
            print("No members to search!!") 
            time.sleep(2)
    elif choice=="4":
        if lista:
            edit_member(lista)
        else:
            print("No members to edit!!") 
            time.sleep(2)
    elif choice=="5":
        if lista:
            remove_member(lista)
        else:
            print("No member to delete!!")
            time.sleep(2)
    elif choice== "6":
        print("Exiting.................")
        break    
    else:
        print("Invalid choice, please try again!!")
        time.sleep(2)
            
