import json5
class User:
    def __init__(self,username,password,mail):
        self.username=username
        self.password=password
        self.email=mail

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn=False
        self.currentUser={}

        # Load Users from .json
        #self.loadUser()
    def LoadUser(self):
        pass
    def register(self,user:User):
        print(type(user))
        self.users.append(user)
        self.savetoFile()
        print("User is created")
        pass
    def login(self):
        pass
    def savetoFile(self):
        list=[]
        for user in self.users:
            print(user)
            list.append(json5.dumps(user))
            print(list)

        with open("users.json","w",encoding="UTF-8") as file:
            json5.dump(list,file)

repository=UserRepository()
while True:
    print('Menu'.center(50,'*'))
    select=input('1-Register\n2-Login\n3-Logout\n-4identity\n5-Exit\nSelect:')
    if select=='5':
        break
    elif select=='1':
        username=input("Username")
        password=input("Password")
        mail=input("Mail")
        user=User(username,password,mail)
        repository.register(user)
    elif select=='2':
        pass
    elif select=='3':
        pass
    elif select=='4':
        pass
    else:
        pass