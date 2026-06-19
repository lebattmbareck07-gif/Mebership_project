from models import Gym_membership_Management
import json
import os
import time
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")
#-------------------------------------------------------------------------------------------------------------------
def save_member(lista):
     with open("Basket.json", "w") as file:
        json.dump(lista,file, indent=4)
#----------------------------------------------------------------------------------------------------------------

def show_member(member):
    Gym_membership_Management(member["first_name"], member["last_name"], member["ID"], member["status"]).display()
#-----------------------------------------------------------------------------------------------------------------------
def create_user(lista):
    clear_screen()
    first_name=input("Enter first name: ")
    last_name=input("Enter last name: ")
    found_id=False
    while not found_id :
        ID=input("Enter membership ID: ")
        if not ID.isdigit():
            print("This spot requires input number, Try again!!")
            continue
        else:
            if any (member["ID"]==ID for member in lista) : 
                print("This ID is already exist, Please enter another ID!")
                continue
            else:
                found_id=True
        status=input("Enter Membership status, Or click enter: ").capitalize() or "Inactive"
    return Gym_membership_Management(first_name, last_name, ID, status)
#--------------------------------------------------------------------------------------------------------------------
def remove_member(lista):
    member_to_delete=None
    while True:
        clear_screen()
        D_member=input("Please enter the Membership ID will Delete or click (Enter) to cancel: ").strip()
        if D_member:
            found_id=False
            for member in lista:
                if D_member==member["ID"]:
                    member_to_delete=member
                    print("Here is the Member!!\n")
                    show_member(member)
                    found_id=True
                    break
            if not found_id:
                if D_member.isdigit():
                    print("The Membership ID entered is not recognized, Try again!!")
                    time.sleep(2)
                    continue
                else:     
                    print("invalid input please try again!!")
                    time.sleep(2)
                    continue
            validation=input("\nAre you sure to delete this Member (Yes or NO): ").strip()
            if validation.lower()=="yes":
                if member_to_delete:
                    lista.remove(member_to_delete)
                    save_member(lista)
                    print("Done,The Member got deleted ")
                    time.sleep(2)
                    break
                else:
                    print("Member not found!!")
                    time.sleep(2)
            elif validation.lower()=="no":
                print("The Member still in the Membership!!")
                time.sleep(2)
                break
            else:
                print("Invalid choice, Try again!")
                time.sleep(2)
                continue
        else:
            break
        
#----------------------------------------------------------------------------------------------------------------
def search_member(lista):
    while True:
        clear_screen()
        print("Search by:\n1. Membership ID\n2. First Name\n3. Membership Status\n4. Cancel")
        choice=input("Enter your choice: ")
        if choice=="1":
            Uid=input("Enter the membership ID to search: ").strip()
            found_id=False
            for member in lista:
                if Uid==member["ID"]:
                    if not found_id:
                        clear_screen()
                        print("Member Found:\n")
                    show_member(member)
                    found_id=True
                    break
            if  found_id:
                time.sleep(3)
                break
            else:
                print("Unfound Member!!!")
                time.sleep(2)
                continue
        elif choice=="2":
            Ufirst_name=input("Enter the first name to search: ").strip()
            found_firstName=False
            for member in lista:
                if Ufirst_name.lower()==member["first_name"].lower():
                    if not found_firstName:
                        clear_screen()
                        print("Members Found:\n")
                    show_member(member)
                    found_firstName=True
            if  found_firstName:
                time.sleep(4)
                break
            else:
                print("Unfound Members!!!")
                time.sleep(2)
                continue
        elif choice=="3":
            Ustatus=input("Enter the status to search: ").strip()
            found_Ustatus=False
            for member in lista:
                if Ustatus.capitalize()==member["status"].capitalize():
                        if not found_Ustatus:
                            clear_screen()
                            print("Members Found:\n")
                        show_member(member)
                        found_Ustatus=True
            if  found_Ustatus:
                time.sleep(4)
                break
            else:
                print("Unfound Members!!!!")
                time.sleep(2)
                continue
        elif choice=="4" or choice.lower()=="cancel":
            break
        else:
            print("Invalid choice, Try again!!!!")
            time.sleep(2)
            continue
#---------------------------------------------------------------------------------------------------------
def displaying_member(lista):
    clear_screen()
    print("Displaying all members.....\n")
    time.sleep(1)
    for member in lista:
       show_member(member)
    time.sleep(4)
#--------------------------------------------------------------------------------------------------------------
def edit_member(lista):
    while True:
        clear_screen()
        right_member=None
        found_id=False
        u_ID=input("Enter The ID you will edit or click enter to cancel: ").strip()
        if u_ID:
            for member in lista:
                if member["ID"]==u_ID:
                    right_member=member
                    if not found_id:
                        print("Here is the Member!!\n")
                    show_member(member)
                    found_id=True
                    time.sleep(2)
                    break
            if not found_id:
                if u_ID.isdigit():
                    print("The Membership ID entered is not recognized, Try again!!")
                    time.sleep(2)
                    continue
                else:     
                    print("invalid input please try again!!")
                    time.sleep(2)
                    continue
            Answer=input("\nWhich one  will you change:\n1. First name\n2. Last name\n3. Membership ID\n4. Status\n5. Cancel\n---->").strip()
            if Answer.capitalize()=="First name" or Answer=="1":
                new_firstname=input("Enter The new first name or click Enter to cancel: ").strip()
                if new_firstname:
                    if right_member: 
                        right_member["first_name"]=new_firstname
                        save_member(lista)
                        print("Done!!")
                        time.sleep(2)
                        break
                    else:
                        print("Not found member!")
                        time.sleep(2)
                else:
                    break
            elif Answer.capitalize()=="Last name" or Answer=="2":
                new_lastname=input("Enter The new last name or click Enter to cancel: ")
                if new_lastname:
                    if right_member:
                        right_member["last_name"]=new_lastname
                        save_member(lista)
                        print("Done!!")
                        time.sleep(2)
                        break
                    else:
                        print("Not found member!")
                        time.sleep(2)
                else:
                    break
            elif Answer.capitalize()=="Membership ID" or Answer=="3":
                new_ID=input("Enter The new Membership ID or click Enter to cancel: ")
                if new_ID:
                    if right_member:
                        if new_ID.isdigit():
                            if any(new_ID==member["ID"] for member in lista):
                                print("This ID is already exist, Try again!!")
                                time.sleep(2)
                            else:
                                right_member["ID"]=new_ID
                                save_member(lista)
                                print("Done!!")
                                time.sleep(2)
                                break
                        else:
                            print("This is not a number, Try again!!")
                            time.sleep(2)
                    else:
                        print("Not found member!")
                        time.sleep(2)
                else:
                    break
            elif Answer.capitalize()=="Status" or Answer=="4":
                new_status=input("Enter The new status or click Enter to cancel: ")
                if new_status:
                    if right_member:
                        right_member["status"]=new_status
                        save_member(lista)
                        print("Done!!")
                        time.sleep(2)
                        break
                    else:
                        print("Not found member!")
                        time.sleep(2)
                else:
                    break
            elif Answer.capitalize()=="Cancel" or Answer=="5":
                print("Process Canceled")
                time.sleep(2)
                break
            else:
                print("Invalid choice!!")
                time.sleep(2)
        else:
            break