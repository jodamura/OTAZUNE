import streamlit as st
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

# DBとのconnectionを作る関数
def get_db_connection():
    return mysql.connector.connect(
        host=host,
        user=database_username,
        password=database_password,
        database="otazunedb",
    )

# 提案を取得する関数
def get_suggestions_by_id(elemid):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT * FROM `suggestion_db` WHERE `ID`=%s"
        cursor.execute(sql, (elemid,))
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results
    except Error as e:
        st.error(f"Error: {e}")
        return []

# 提案情報を表示する関数
def display_suggestion(suggestion):
    st.write("提案ID:", suggestion["suggestionID"])
    st.write("提案日時:", suggestion["suggestiondate"])
    st.write("提案者:", suggestion["suggester"])
    st.write("メールアドレス:", suggestion["mailaddress"])
    st.write("提案内容:", suggestion["suggestion"])

# Streamlitアプリケーション
def main():
    st.title("提案一覧ページ")

    # ユーザーにIDを入力してもらう
    elemid = st.number_input("提案を検索するIDを入力してください", min_value=1, step=1)

    # IDを指定して提案を取得
    suggestions = get_suggestions_by_id(elemid)

    # 提案の一覧を表示
    if suggestions:
        st.subheader(f"ID {elemid} の提案一覧")
        for suggestion in suggestions:
            display_suggestion(suggestion)
            st.markdown("---")
    else:
        st.write("提案が見つかりませんでした。")

if __name__ == "__main__":
    main()
