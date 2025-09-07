# 透過 uvicorn，告訴他檔案在哪裡，並啟動 FastAPI
# uvicorn main:app --reload
# main 是檔案名稱，app 是 FastAPI 物件名稱

# 處理網址的埠號
# 指令：uvicorn main:app --reload --port 3000


# 基本路由設定範例
from typing import List
from fastapi import FastAPI, Query, Path

app = FastAPI() # FastAPI 物件放在變數 app 裡面

# 建立網站首頁 「index」名稱可以自己取
# @app.get("/")
# def index():
#     return {"x":3,"y":4}

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

# practice 2 - 路由與「要求字串」的練習
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

# 輸入資料驗證
# item_id: Annotated[int, None] 表示 item_id 是 int 類型，且沒有其他限制
# 接收浮點數：float
# 更多限制：
#   item_id:Annotated[int,Path(gt=3,lt=10)]
#   Path 代表針對路徑參數做驗證
#   gt : > | lt : < | ge : >= | le : <=

# 加上資料驗證的好處，假設打了 getItem 但是 item_id 傳入了字串，就會回應以下錯誤，並且會被擋掉，不會進到主要的程式
# 如果沒有加資料驗證，就會是 內部伺服器錯誤 (500 Internal Server Error)，因為程式會嘗試將字串轉換為 float，失敗後沒有處理這個錯誤。
# 422 Unprocessable Entity
# {
#   "detail": [
#     {
#       "type": "float_parsing",
#       "loc": [
#         "path",
#         "item_id"
#       ],
#       "msg": "Input should be a valid number, unable to parse string as a number",
#       "input": "abc"
#     }
#   ]
# }

from typing import Annotated
@app.get("/item/{item_id}")
def getItem(item_id:Annotated[float,None]):
    id = float(item_id)
    return { "result": id }

@app.get("/item/{item_id}")
def getItem2(item_id: Annotated[int, Path(gt=3, lt=100)]):
    return { "result":  item_id }

# /items?store_id=1&item_id=10
# Query 代表針對查詢參數做驗證
@app.get("/items")
def getItems(
    store_id:Annotated[int,Query(gt=0)],
    item_id:Annotated[int,Query(gt=0, le=100)]
):
    
    return {"result": f"{store_id} , {item_id}"}

# 練習：處理路徑 /echo/{name}
@app.get("/echo/{name}")
def echoName(name:Annotated[str,Path(min_length=1, max_length=10)]):
    return {"echo": name}


# 練習：回應格式 response
from fastapi.responses import JSONResponse
# 即使沒用 JsonResponse，fastapi 也是預設將回應轉換為 JSON 格式
@app.get("/hello-message")
def index():
    return JSONResponse({"message": "Hello, World!"})

# 練習：回應格式 純字串
# /text?text=Hello
from fastapi.responses import PlainTextResponse
@app.get("/text")
def textTest(text):
    return PlainTextResponse(f"<h2>Hello, World!</h2> {text}")

# 練習：回應格式 HTML
from fastapi.responses import HTMLResponse
@app.get("/html")
def htmlTest():
    return HTMLResponse("<h1>Hello, World!</h1> <p>This is a paragraph.</p>")

# 練習：回應檔案-HTML
from fastapi.responses import FileResponse
@app.get("/file")
def fileTest():
    return FileResponse("home.html")

# 練習：回應檔案-圖片
@app.get("/img/logo")
def imgLogo():
    return FileResponse("logo.png")

# 練習: 重新導向 Redirect
# /redirect
from fastapi.responses import RedirectResponse
@app.get("/redirect")
def redirectTest():
    return RedirectResponse("/")


# 靜態檔案（回傳給前端）：沒有執行任何程式邏輯，直接回傳檔案內容
# example
from fastapi.responses import FileResponse
@app.get("/file/test")
def index():
    return FileResponse("home.html")

# 處理多個靜態檔案
# 靜態檔案的處理通常會擺在最下方，才不會影響其他路由
# http://127.0.0.1:8000/public/home.html
# http://127.0.0.1:8000/public/img/logo.png 因為在 www 裡面的 img 資料夾
from fastapi.staticfiles import StaticFiles # StaticFiles 可以「統一」處理靜態檔案
app.mount("/public",StaticFiles(directory='www'))

# 上面的方法，需要在路徑帶上檔案名稱，如果想要完成像是「路徑是首頁，但會對應到一個 html 檔案」時的做法
# 要將對應的 html 檔案命名為 index.html
app.mount("/", StaticFiles(directory="www", html=True))
