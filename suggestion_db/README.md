# 24/4/21 odamura追記
MySQLにはsuggestion_db.csvのダミーデータを3件入れてある

「suggestionID」はAUTO_INCREMENTなのでsuggestion_db.csvには記載なし
「ID」はMySQLのotazunedb.tourreservationにデータ格納する際にAUTO_INCREMENTで生成されたIDと同一。（提案とこのIDを紐づける必要があり）
「suggestiondate」はtimestamp CUREENT_TIMESTAMPで生成予定