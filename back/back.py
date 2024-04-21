# 必要なライブラリのimport
from fastapi import FastAPI, Depends, HTTPException
from typing import Optional, List
from pydantic import BaseModel

# SQL用
import mysql.connector
from mysql.connector import Error

# env読み込み用
import os
from os.path import join, dirname
from dotenv import load_dotenv


# 環境変数envファイルからの取得用
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# 環境変数の取得
host = os.environ.get("host")
database_username = os.environ.get("database_username")
database_password = os.environ.get("database_password")


########################### FOR buyitem ##############################
class PurchaseItem(BaseModel):
    name: str
    price: int
    barcode: str
    product_id: int
    member_id:str
######################################################################



app = FastAPI()
# ターミナルでuvicorn main:app --reload（mainはファイル名）


# CORS設定 #############################################################
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost:3000",  # フロントエンドのオリジン
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
########################################################################




############################################################
# 関数
############################################################
# DBとのconnectionを作る関数
def get_db_connection():
    return mysql.connector.connect(
        host=host,
        user=database_username,
        password=database_password,
        database="otazunedb",
    )


def getalldata():
    # データベースに接続
    connection = get_db_connection()
    
    # 辞書形式で結果を取得するためのcursorの作成
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM `tourreservation`"
    cursor.execute(sql,)
    results = cursor.fetchall()
    # cursorを閉じる
    cursor.close()
    # データベース接続を閉じる
    connection.close()
    return results


########################################################
# 下記インスタンス
########################################################
# SQLからすべてのデータ取得
@app.get("/")
async def getdata():
    res = getalldata()
    return res

