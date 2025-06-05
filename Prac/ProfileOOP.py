class UserProfile:
    def __init__(self, name, age, email, password, location):
        self.name = name
        self.age = age
        self.email = email
        self.password = password
        self.location = location

    def displayInfo(self):
        return f"{self.name}, {self.age}, {self.location}"

class UserProtected(UserProfile):
    def displayUserAccount(self):
        return f"{self.email}, {self.password}"
    

 # obj = UserProfile("dustin", 20, "dom@gmail.com","Laguna") creating manual Object 

arr = [['name', 21, 'email', 'password', 'location']]

def createUser():
    username = input("Enter Name: ")
    userage = int(input("Enter Age: "))

    useremail = input("Enter Email: ")
    userpassword = input("Enter Password: ")

    userlocation = input("Enter Location: ")

    arr.append([username, userage, useremail, userpassword, userlocation])
    print(arr)

    return UserProtected(username, userage, useremail, userpassword, userlocation)

def loginUser(arr):

    useremail = input("Enter Email: ")
    userpassword = input("Enter Password: ")

    for user_data in range(len(arr)):
        if useremail == user_data[2] and userpassword == user_data[3]:
            user = UserProtected(user_data[0], user_data[1], user_data[2],user_data[3], user_data[4])
            print(f"Welcome {user.name}")
                
    
    print("Invalid User Credentials")

def userChoice():
    choice = int(input("Enter Choice 1 - Display Information | 2 - Display User Account: "))

    if choice == 1:
        print(user.displayInfo())

    elif choice == 2:
        print(user.displayUserAccount())
    
    else: print("Wrong Choice")


while True:
    cred = int(input("Enter 1 - Login | Enter 2 - Register"))

    if cred == 1:
        loginUser(arr)
    
    if cred == 2:
        user = createUser()


    userChoice()

    

    