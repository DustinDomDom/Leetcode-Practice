class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('User Created!')

    def __repr__(self):
        return f'Username = {self.username}, Name = {self.name}, Email = {self.email}'
    
    def __str__(self):
        return self.__repr__()
    


class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list(self):
        return self.users

Database = UserDatabase()



Uname = input("Enter Username")
Pname = input("Enter Name")
mail = input("Enter Email")

userdetail = User(Uname, Pname, mail)
Database.insert(userdetail)

while True:
    choice = int(input("Enter Choice 1. Insert | 2. Find | 3. Update | 4. List all | 5. Exit"))

    if choice == 1:
        Uname = input("Enter Username")
        Pname = input("Enter Name")
        mail = input("Enter Email")

        userdetail = User(Uname, Pname, mail)
        Database.insert(userdetail)

    if choice == 2:
        Uname = input("Enter Username to find")

        user = Database.find('daddy')
        print(user)

    if choice == 3:
        pass

    if choice == 4:
        print(Database.list())

    else: print("Whaat?")