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

* カードの色を変えられる
  
  ```html
  <div class="card text-white bg-primary">
  ```
  
* todo一覧画面のカードをドラッグできるようにしてるのはjqueryの機能。

  ```js
  $(function(){
  	$("#{{entry.id}}body").draggable();
  })
  ```

* 以下を記述しないと入力時の改行が反映されない

  ```html
  <p style="white-space: pre-wrap">{{entry.detail}}</p>
  ```

* 画像のトリミングメモ

  ```
  821
  1127
  790
  960	
  ```

* データ登録直後に、自動裁判のidを取得したいときは、flushを挟む。

  ```python
      #todoの新規作成処理を実装
      form = ToDoMaster(
          name=request.form['name'],
          detail=request.form['detail'],
          dead_line=request.form['dead_line'] if request.form['dead_line'] else "9999-12-31"
      )
      db.session.add(form)
      #一度flushしないとidが取得できない
      db.session.flush()
      #タスク名の記入がなければidをタスク名にする。
      if not form.name:
          form.name= "task#"+ str(form.id)
      db.session.commit()
  ```

* python側からjs起動したいときは、scriptタグを返せばいい

  ```python
      script ="""<script>
              window.opener.location.reload();
              window.close();
              </script>"""
      return script
  ```

* show.htmlとedit.htmlでは、あえてそれぞれ違うやり方で自ウインドウのcloseと呼び出し元を更新するロジックを実現している。

  show.htmlはfetchでpostし、自前でjsを実行。edit.htmlでformからpostした先のpython側でscriptタグを返す。



## # 実装していきたいこと

* タグで検索など
* 優先度順に色を付けたり
* 削除機能
* 完了機能



## # 必要なライブラリ

```
pip install Flask-SQLAlchemy
```

