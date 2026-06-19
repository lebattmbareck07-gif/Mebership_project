class Gym_membership_Management:
    def __init__(self, first_name, last_name, ID, status="Inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.ID=ID
        self.status=status.capitalize()
    def display(self):
       print(f"First Name: {self.first_name}")
       print(f"Last Name: {self.last_name}")
       print(f"Membership ID: {self.ID}")
       print(f"Membership status: {self.status}")
       print("-"*27)
    def to_dict(self):
        return {"first_name":self.first_name,
                "last_name":self.last_name,
                "ID":self.ID,
                "status":self.status
        }