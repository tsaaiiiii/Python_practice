# 透過 uvicorn，告訴他檔案在哪裡，並啟動 FastAPI
# uvicorn main:app --reload
# main 是檔案名稱，app 是 FastAPI 物件名稱

# 處理網址的埠號
# 指令：uvicorn main:app --reload --port 3000


# 基本路由設定範例
from typing import List
from fastapi import FastAPI, Query

app = FastAPI() # FastAPI 物件放在變數 app 裡面

# 建立網站首頁 「index」名稱可以自己取
@app.get("/")
def index():
    return {"x":3,"y":4}

@app.get('/data')
def getData():
    return {"name":"John", "age":30, "city":"New York"}


# 路徑參數 Path Parameters
# 動態路由設定語法
# @app.get("/固定字首/{參數名稱}")
# def 處理函式名稱(參數名稱: 類型):
#     return 

# example 根據使用者 id 回應不同訊息
@app.get("/user/{user_id}")
def getUser(user_id):
    return {"user_id": user_id, "message": f"Hello User, {user_id}"}

# practice 1 - 路由與參數的練習
# 讓前端可以透過網址，輸入一個數字，後端把輸入的數字做平方後回傳給前端
@app.get("/square/{number}")
def squareNumber(number:int):
    squared_value  = number**2
    return { "origin" : number, "squared": squared_value }

# practice 2 - 路由與要求字串的練習
# 處理路徑 /greet?name=John
@app.get("/greet")
def greet(name):
    return { "message": f"Hello, {name}!" }

# 處理路徑 /multiply?num1=3&num2=4
@app.get("/multiply")
def multiply(num1: int, num2: int):
    result = num1*num2
    return { "result" : result}

# 處理路徑 /product?id=3&id=4&id=10
@app.get("/product")
def product(id: List[int] = Query(...)):
    return {"ids": id}