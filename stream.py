print('hello')
from fastapi import FastAPI
from pydantic import BaseModel

user_db = {
    'jack': {'userid':0,'username': 'jack', 'date_joined': '2021-12-01', 'location': 'New York', 'age': 28},
    'jill': {'userid':1,'username': 'jill', 'date_joined': '2021-12-02', 'location': 'Los Angeles', 'age': 19},
    'jane': {'userid':2,'username': 'jane', 'date_joined': '2021-12-03', 'location': 'Toronto','age': 52}
}

class User(BaseModel):
    username: str
    userid : int 
    date_joined: str
    location: str
    age: int

class Car(BaseModel):
      numofdoors: int 
      model: str
      is_ev: bool  

app = FastAPI()

@app.get('/')
def get_welcome():
    return {'Output': 'My fast firstapi'}


@app.get('/users')
def get_users():
    list_users = list(user_db.values())
    return list_users

# specific username or user 
@app.get('/users/{uname}')
def get_user(name:str):
    user_name = user_db[name]
    return user_name

 #query based on criteria

@app.get('/users_limit')
def get_by_query(_from: int,_to :int):
    user_list = list(user_db.values())
    return user_list[_from:_to]