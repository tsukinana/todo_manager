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

#for_confirm=ToDoMaster()
#for_confirm.id=1
#for_confirm.name="umbreon"
#for_confirm.detail="pokemon"
#for_confirm.remarks=None
#for_confirm.tag_id=None
#for_confirm.create_date=datetime.now()
#for_confirm.update_date=datetime.now()
#for_confirm.dead_line=datetime.now()
#for_confirm.complate_date=datetime.now()
#for_confirm.complate_flag=0
#for_confirm.frozen_flag=0
#for_confirm.priority_rank=0
#db.session.add(for_confirm)
#db.session.commit()

from todo_manager.views import entries