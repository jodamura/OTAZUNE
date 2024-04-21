# 納品時、中井さんコメント
https://github.com/nakkan14/ultraodamura
MySQLのpasswordは「odamura.py」「sql_drop_table.py」ファイル共に空白としておりますので、
手元で確認される際はパスワードを入力してお使いください。
①Azure DB for MYSQLを立ち上げ。
②sql_drop_table.py　を実行。
③csvファイルがDBに格納される。
④odamura.py　を実行。
⑤LINE文面が生成される。
なお、日本語への翻訳までは実装できておりません。

# 24/4/21 odamura追記
LINE文を生成するodamura.pyは今回使わないので削除
csvを「OMAKASEdatabase.csv」→「tour_reservation_db.csv」に名前変更

環境変数をうまく使えなかったので、MYSQL_PASSWORD をベタ打ち。
Githubに上げる際は「sql_drop_table.py」のMYSQL_PASSWORDは削除する。

sql_drop_table.pyでレガシー資産の予約データをMySQLに格納する仕組み。
格納された予約データの中の情報をもとに、要望一覧ページを作成（tokky対応）