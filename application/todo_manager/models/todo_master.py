#!/usr/bin/env python
#-*-coding: utf-8-*-

from todo_manager import db
from datetime import datetime

class ToDoMaster(db.Model):
    __tablename__ ="todo_master"
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=True)
    detail = db.Column(db.String)
    remarks = db.Column(db.String)
    tag_id = db.Column(db.String)
    create_date = db.Column(db.TIMESTAMP,nullable=False,default=datetime.now)
    update_date = db.Column(db.TIMESTAMP,nullable=False,default=datetime.now)
    dead_line = db.Column(db.TIMESTAMP)
    complate_date = db.Column(db.TIMESTAMP)
    complate_flag = db.Column(db.Integer,nullable=False,default=0)
    frozen_flag = db.Column(db.Integer,nullable=False,default=0)
    priority_rank = db.Column(db.Integer,nullable=False,default=0)
    delete_flag = db.Column(db.Integer,nullable=False,default=0)
    
    def toDict(self):
        return {
            "id":self.id,
            "name":self.name,
            "detail":self.detail,
            "remarks":self.remarks,
            "tag_id":self.tag_id,
            "create_date":self.create_date,
            "update_date":self.update_date,
            "dead_line":self.dead_line,
            "complate_date":self.complate_date,
            "complate_flag":self.complate_flag,
            "frozen_flag":self.frozen_flag,
            "priority_rank":self.priority_rank,
            "delete_flag":self.delete_flag
        }