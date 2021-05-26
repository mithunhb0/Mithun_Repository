import requests
import json

BASE_URL='http://127.0.0.1:8000/'
END_POINT='cric/'

def get_resource(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    response=requests.get(BASE_URL+END_POINT,data=json.dumps(data))
    print(response.status_code)
    print(response.json())


def get_resource(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    response=requests.get(BASE_URL+END_POINT,data=json.dumps(data))
    print(response.status_code)
    print(response.json())


def create_resource():
    name = input('Enter the Name of the Cricketer:\t')
    jersey_number = int(input('Enter the Jersey Number of Cricketer:\t'))
    age = int(input('Enter the Age of the Cricketer:\t'))
    ipl_team = input('Enter the IPL team he belongs to :')
    cric_data = {'name':name,'jersey_number':jersey_number,'age':age,'ipl_team':ipl_team}
    response = requests.post(BASE_URL+END_POINT,data=json.dumps(cric_data))
    print(response.status_code)
    print(response.json())


def update_resource_partially(id):
    update_data={'id':id,'name':'mithun','ipl_team':'csk'}
    response = requests.put(BASE_URL+END_POINT,data=json.dumps(update_data))
    print(response.json())
    print(response.status_code)

def update_resource_completly(id):
    name = input('Enter  the Name of the Cricketer, to update:\t')
    jersey_number = int(input('Enter the Jersey Number of Cricketer, to update:\t'))
    age = int(input('Enter the Age of the Cricketer, to update:\t'))
    ipl_team = input('Enter the IPL team he belongs to, to update :')
    update_data={'id':id,'name':name,'jersey_number':jersey_number,'age':age,'ipl_team':ipl_team}
    response = requests.put(BASE_URL+END_POINT,data=json.dumps(update_data))
    print(response.json())
    print(response.status_code)

def delete_resource(id=None):
    data={'id':id}
    response = requests.delete(BASE_URL+END_POINT,data=json.dumps(data))
    print(response.json())
    print(response.status_code)


while True:
    print("CRUD OPERATION (Single End Point Rule)")
    print("1.Select complete data")
    print("2.Select single data")
    print("3.Create the data")    
    print("4.Update the data partially")
    print("5.Update the data completly")
    print("6.Delete the data")
    print("7.Exit")
    
    choice=int(input("Enter your choice:"))
    if choice==1:
        get_resource()
  
    elif choice==2:
        id = int(input('Enter the ID:\t'))
        get_resource(id)

    elif choice==3:
        create_resource()

    elif choice==4:
        id = int(input('Enter the ID:\t'))
        update_resource_partially(id)
    
    elif choice==5:
        id = int(input('Enter the ID:\t'))
        update_resource_completly(id)
    
    elif choice==6:
        id = int(input('Enter the ID:\t'))
        delete_resource(id)

    elif choice==7:
        break
    else:
        print("Wrong Choice !!!!!")