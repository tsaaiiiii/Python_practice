from fastapi import FastAPI
app = FastAPI() # FastAPI 物件

#建立網站首頁 「index」名稱可以自己取
@app.get("/")
def index():
    return {"x":3,"y":4}


# 透過 uvicorn，告訴他檔案在哪裡，並啟動 FastAPI
# uvicorn main:app --reload
# main 是檔案名稱，app 是 FastAPI 物件名稱


# 處理網址的埠號
# 指令：uvicorn main:app --reload --port 3000


