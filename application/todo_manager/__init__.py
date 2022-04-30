#!/usr/bin/env python
#-*-coding: utf-8-*-

from flask import Flask

app = Flask(__name__)
app.config.from_object("todo_manager.conf.config")

@app.route("/")
def show_entries():
    return "hello"