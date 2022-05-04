# # todo_maneger



## DB定義

#### TODO_MASTER

| #    | カラム(物理名) | 論理名     | 型        | 制約      | 説明            |
| ---- | -------------- | ---------- | --------- | --------- | --------------- |
| 1    | id             | ID         | INTEGER   | PRIME_KEY | ユニークキー    |
| 2    | name           | タスク名   | VARCHAR   |           | タスク名        |
| 3    | detail         | 内容       | VARCHAR   |           | タスク内容      |
| 4    | remarks        | 備考       | VARCHAR   |           | 備考            |
| 5    | tag_id         | タグID     | VARCHAR   |           | タグマスターKEY |
| 6    | create_date    | 作成日     | TIMESTAMP | not null  | 作成日          |
| 7    | update_date    | 更新日     | TIMESTAMP | not null  | 更新日          |
| 8    | dead_line      | 期限日     | TIMESTAMP |           | 期限日          |
| 9    | complate_date  | 完了日     | TIMESTAMP |           | 完了日          |
| 9    | complate_flag  | 完了フラグ | INTEGER   | not null  | 完了フラグ      |
| 10   | frozen_flag    | 凍結フラグ | INTEGER   | not null  | 凍結フラグ      |
| 11   | priority_rank  | 優先ランク | INTEGER   | not null  | 優先ランク      |
| 12   | delete_flag    | 削除フラグ | INTEGER   | not null  | 削除フラグ      |



## # 開発メモ

* 当初sqlite3で直にsql書いていたが、sqlite3の制約で別のスレッドで作ったコネクションやカーソルが別のスレッドで流用できないことから、毎回dbコネクションを貼る必要があり、無駄が多かったためflask_sqlalchemyに移行した。



## # 必要なライブラリ

```
pip install Flask-SQLAlchemy
```

