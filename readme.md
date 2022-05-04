# # todo_maneger



## DB定義



#### TODO_MASTER

| #    | カラム(物理名) | 論理名     | 型   | 制約      | 説明            |
| ---- | -------------- | ---------- | ---- | --------- | --------------- |
| 1    | id             | ID         | INT  | PRIME_KEY | ユニークキー    |
| 2    | name           | タスク名   | TEXT |           | タスク名        |
| 3    | detail         | 内容       | TEXT |           | タスク内容      |
| 4    | remarks        | 備考       | TEXT |           | 備考            |
| 5    | tag_id         | タグID     | INT  |           | タグマスターKEY |
| 6    | create_date    | 作成日     | TEXT |           | 作成日          |
| 7    | update_date    | 更新日     | TEXT |           | 更新日          |
| 8    | dead_line      | 期限日     | TEXT |           | 期限日          |
| 9    | complate_date  | 完了日     | TEXT |           | 完了日          |
| 9    | complate_flag  | 完了フラグ | TEXT |           | 完了フラグ      |
| 10   | frozen_flag    | 凍結フラグ | TEXT |           | 凍結フラグ      |
| 11   | priority_rank  | 優先ランク | TEXT |           | 優先ランク      |

