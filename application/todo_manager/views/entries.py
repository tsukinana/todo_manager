#!/usr/bin/env python
#-*-coding: utf-8-*-
from flask import request,redirect,url_for,render_template,flash,session
from todo_manager import app
from datetime import datetime

@app.route("/")
def show_entries():
    #全てのtodoを表示
    entries = [
        {
            "id":1,
            "title":"初めての投稿",
            "text":"内容",
            "created_at":datetime.now(),
        },
        {
            "id":2,
            "title":"2つめの投稿",
            "text":"内容",
            "created_at":datetime.now(),
        },
        
    ]
    return render_template("entries/index.html",entries=entries)

@app.route("/entries",methods=["POST"])
def add_entry():
    #todoの新規作成処理を実装
    return "新しいtodoが出来ました"

@app.route("/entries/new",methods=["GET"])
def new_entry():
    #todoの入力フォームを実装
    return render_template("entries/new.html")

@app.route('/entries/<int:id>',methods=['GET'])
def show_entry(id):
    #todoを取得
    entry= {
            "id":1,
            "title":"初めての投稿",
            "text":"内容",
            "created_at":datetime.now(),
        }
    return render_template("entries/show.html",entry=entry)

@app.route('/entries/<int:id>/edit',methods=['GET'])
def edit_entry(id):
    #todoの編集フォームを表示
    entries = [
        {
            "id":1,
            "title":"初めての投稿",
            "text":"内容",
            "created_at":datetime.now(),
        },
        {
            "id":2,
            "title":"2つめの投稿",
            "text":"内容",
            "created_at":datetime.now(),
        },
    ]
    entry = None
    for e in entries:
        if e["id"] == id:
            entry = e
    return render_template("entries/edit.html",entry=entry)

@app.route('/entries/<int:id>/update',methods=['POST'])
def update_entry(id):
    #todoの更新処理を実装
    return f"todo{id}が更新されました"

@app.route('/entries/<int:id>/delete',methods=['POST'])
def delete_entry(id):
    #todoの削除処理を実装
    return f"todo{id}が削除されました"