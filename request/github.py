import requests
import json


class gitHub():
    def __init__(self):
        self.api_url='https://api.github.com'
        self.token="499c24444244e304bf7e947f72b91e4cc621c55c"
    def getUser(self,user):
        response=requests.get(self.api_url+'/users/'+user)
        return response.json()
    def getRepositories(self,user):
        response=requests.get(self.api_url+'/users/'+user+'/repos')
        return response.json()
    def createRepositories(self,name):
        response=requests.post(self.api_url+'/user/repos?access_token='+self.token,json=
        {"name":name,
        "description": "This ",
        "homepage": "https://github.com",
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True})




git=gitHub()    
while True:
    choose=input("1-Find USER\n2-Get Repositories\n3-Create Repository\n4-Exit\nChoose: ")
    if choose=="4":
        break
    else:
        if choose=='1':
            _user=input("Username: ")
            response=git.getUser(_user)
            print(f"name: {response['name']}\npublic_repo: {response['public_repos']}\nfallowers: {response['followers']}\n")
        elif choose=='2':
            _user=input("Username: ")
            response=git.getRepositories(_user)
            for repo in response:
                print(f"Repo Name: {repo['name']}")
        elif choose=='3':
            _name=input("Give a name for repo:  ")
            response=git.createRepositories(_name)
        else:
            print('invaild choice')

