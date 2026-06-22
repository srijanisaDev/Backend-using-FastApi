from fastapi import FastAPI ,Header
from typing import Optional 
from pydantic import BaseModel

from src.books.routes import book_router

app = FastAPI()

app.include_router(book_router, prefix="/api/v1", tags=["books"])

@app.get('/')
async def read_root():
    return {"message" : "Hello world"}

@app.get('/greet')
async def greet_name(name:Optional[str] = "User" , age:int = 0) -> dict:
    return {"message":f"Hello {name}" , "age":age}

class BookCreateModel(BaseModel):
    title : str
    author : str

@app.post('/create_book')
async def create_book(book_data:BookCreateModel):
    return {
        "title":book_data.title,
        "author": book_data.author
    }


@app.get('/get_headers')
async def get_headers(
    accept:str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host : str = Header(None)
):
    request_headers = {}
    request_headers['Accept'] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-agent"] = user_agent
    request_headers["Host"] = host

    return request_headers


@app.get('/items/{item_id}')
async def get_items(q:Optional[str] = None, item_id:int = 0) -> dict:
    return {"item id":item_id , "q":q}


class UserModel(BaseModel):
    username : str
    email : str
    age:int
    role: str = "viewer"
    bio : Optional[str] = None


@app.post('/create_user')
async def create_user(user_data : UserModel) -> dict:
    return {
        "username" : user_data.username,
        "email": user_data.email,
        "age": user_data.age,
        "role": user_data.role,
        "bio": user_data.bio        
    }    



@app.put('/update_book/{book_id}')
async def update_book(book_id: int, book_data: BookCreateModel) -> dict:
    return {
        "book_id": book_id,
        "title": book_data.title,
        "author": book_data.author
    }

