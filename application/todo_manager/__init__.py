#!/usr/bin/env python
#-*-coding: utf-8-*-

from flask import Flask
from todo_manager.lib.log import org_get_logger
import flask_sqlalchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_object("todo_manager.conf.config")
db = flask_sqlalchemy.SQLAlchemy(app)

from todo_manager.models.todo_master import ToDoMaster
db.create_all()

from todo_manager.views import entries