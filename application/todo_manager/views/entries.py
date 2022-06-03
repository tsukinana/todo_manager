#!/usr/bin/env python
#-*-coding: utf-8-*-
import os
from unicodedata import name
from flask import request,redirect,url_for,render_template,flash,session
from todo_manager import app,ToDoMaster,org_get_logger,db
from datetime import datetime

logger = org_get_logger(__name__)

@app.route("/")
def show_entries():
    """最初の画面 taskを一覧表示する"""
    row = ToDoMaster.query.all()
    
    #todo結果のログ出力用
    for entry in row:
        logger.info(entry.toDict())
    
    #static/imageのファイル名取得
    image_list = os.listdir("todo_manager/static/image/")
    image_list.remove(".gitignore")
    logger.info(image_list)
        
    return render_template("entries/index.html",entries=row,image_list=image_list)

@app.route("/entries",methods=["POST"])
def add_entry():
    """taskの新規作成処理"""
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
    return redirect(url_for("show_entries"))

@app.route("/entries/new",methods=["GET"])
def new_entry():
    """taskの新規作成画面に遷移"""
    return render_template("entries/new.html")

@app.route('/entries/<int:id>',methods=['GET'])
def show_entry(id):
    """taskの詳細画面"""
    entry = ToDoMaster.query.get(id)
    return render_template("entries/show.html",entry=entry)

@app.route('/entries/<int:id>/edit',methods=['GET'])
def edit_entry(id):
    """taskの編集画面に遷移"""
    entry = ToDoMaster.query.get(id)
    return render_template("entries/edit.html",entry=entry)

@app.route('/entries/<int:id>/update',methods=['POST'])
def update_entry(id):
    """taskの更新処理"""
    entry = ToDoMaster.query.get(id)
    entry.name=request.form['name']
    entry.detail=request.form['detail']
    db.session.commit()
    flash("タスクを更新しました。")
    return redirect(url_for("show_entries"))

@app.route('/entries/<int:id>/delete',methods=['POST'])
def delete_entry(id):
    """taskの削除処理"""
    ToDoMaster.query.filter_by(id = id).delete()
    db.session.commit()
    flash("タスクを削除しました。")
    return redirect(url_for("show_entries"))