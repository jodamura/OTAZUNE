■ backend
cd back
uvicorn back:app --reload

■ frontend
cd front
npm start

---
■ tour_reservation_db　
レガシーIT資産である予約情報の更新に利用する。今はもう使わない。
レガシーシステムより予約情報をcsvファイルで出力したものをMySQLに格納するためのコードとCSVファイル。
csvファイル「tour_reservation_db.csv」がMySQLテーブル名「tourreservation」に格納される。

■ suggestion_db
提案のダミーデータ作成に使用した。今後もう使わない。
csvファイル「suggestion_db.csv」をMySQLテーブル名「suggestion_db」に格納した。