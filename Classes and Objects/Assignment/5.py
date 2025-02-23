class Team:
    def __init__(self):
        self.members = []
        n = int(input("Enter the Total Number of Team Members: "))
        for i in range(n):
            name = input(f"Enter {i+1} Team Member's Name: ")
            self.members.append(name)
        print("Team members have been added.")
        self.show()

    def show(self):
        for i in range(len(self.members)):
            print(f"{i+1}- {self.members[i]}")
obj = Team()