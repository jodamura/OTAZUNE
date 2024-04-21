■ backend
cd back
uvicorn back:app --reload

■ frontend
cd front
npm start

※「node_modules」はGithubにコミットしていない。非常に大きいファイルなのでコミットが推奨されていない。
package.jsonとpackage-lock.jsonファイルにプロジェクトの依存関係とその正確なバージョンが指定されているので
他の開発者がプロジェクトをクローンした後、npm installを実行するだけで、必要な依存関係を正確にインストールすることができる。

■ tour_reservation_db　
MYSQL_PASSWORDは削除してある。
レガシーIT資産である予約情報の更新に利用する。今はもう使わない。
レガシーシステムより予約情報をcsvファイルで出力したものをMySQLに格納するためのコードとCSVファイル。
csvファイル「tour_reservation_db.csv」がMySQLテーブル名「tourreservation」に格納される。


■ suggestion_db
MYSQL_PASSWORDは削除してある。
提案のダミーデータ作成に使用した。今後もう使わない。
csvファイル「suggestion_db.csv」をMySQLテーブル名「suggestion_db」に格納した。