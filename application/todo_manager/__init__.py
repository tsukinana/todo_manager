#!/usr/bin/env python
#-*-coding: utf-8-*-

from flask import Flask
from todo_manager.lib.log import org_get_logger
from todo_manager.conf.db_config import create_todo_master
import todo_manager.models

app = Flask(__name__)
app.config.from_object("todo_manager.conf.config")

from todo_manager.views import entries