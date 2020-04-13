import requests
import json
result=requests.get('https://api.exchangeratesapi.io/latest?base=USD')
result=result.json()
response=result['rates']

while True:
    key=input("Give a Currency('TRY'): ")
    key2=input("Give a Currency to translate (Q)Exit: ")
    num=int(input("Give Number: "))
    if key2=='q':
        break
    _result=(num*(response[key2]/response[key]))
    print(_result)




"""for i,j in response.items():
   print(type(j))
   break"""