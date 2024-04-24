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

def getsugdata(elemid):
    # データベースに接続
    connection = get_db_connection()
    
    # 辞書形式で結果を取得するためのcursorの作成
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT * FROM `suggestion_db` WHERE `ID`=%s"
    cursor.execute(sql,(elemid,))
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

@app.get("/getsug/{elemid}")
async def getsuggestiondata(elemid:int):
    res = getsugdata(elemid)
    return res

@app.post("/add_suggestion")
async def add_suggestion(suggestion_data: dict):
    # データベースに接続
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        # 新しい提案の情報を提供
        new_sug = {
            'ID': suggestion_data.get('ID'),
            'suggester': suggestion_data.get('suggester'),
            'mailaddress': suggestion_data.get('mailaddress'),
            'suggestion': suggestion_data.get('suggestion')
        }

        # 新しい提案をデータベースに挿入
        sql = "INSERT INTO `suggestion_db` (`ID`, `suggester`, `mailaddress`, `suggestion`) VALUES (%(ID)s, %(suggester)s, %(mailaddress)s, %(suggestion)s)"
        cursor.execute(sql, new_sug)
        # コミットを実行して変更を保存
        connection.commit()
        return {"message": "提案が正常に追加されました。"}

    except mysql.connector.Error as error:
        # エラーが発生した場合、トランザクションをロールバック
        connection.rollback()
        return {"error": f"エラー: {error}"}

    finally:
        # cursorを閉じる
        cursor.close()
        # データベース接続を閉じる
        connection.close()
