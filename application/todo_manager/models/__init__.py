#!/usr/bin/env python
#-*-coding: utf-8-*-

from todo_manager import org_get_logger
from todo_manager import create_todo_master
import os
import sqlite3


logger = org_get_logger(__name__)

dbname = "UMBREON.db"
conn = sqlite3.connect(dbname)
logger.debug("connect UMBREON.db")

cur = conn.cursor()
cur.execute(
    create_todo_master
)
conn.commit()

#cur.execute(
#    "INSERT INTO todo_master VALUES('1','PIKACHU','POKEMON','ねずみポケモン',NULL,datetime('now', 'localtime'),datetime('now', 'localtime'),datetime('now', 'localtime'),datetime('now', 'localtime'),0,0,0)"
#)

#conn.commit()

cur.execute(
    'SELECT * FROM TODO_MASTER'
)

logger.info(cur.fetchall())

cur.close()
conn.close()