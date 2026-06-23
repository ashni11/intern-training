from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello {name}"}

data = [
    {"id":1,
     "name" :"manojkumar"},
     {"id":2,
     "name" :"ashni"} 
]


@app.get("/books/{book_id}")
def hww(book_id:int):
    
    for i in data:
        if i["id"] == book_id:
            return i
        