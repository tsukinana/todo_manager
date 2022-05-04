create_todo_master="CREATE TABLE IF NOT EXISTS todo_master"\
                   "("\
                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"\
                   "name TEXT,"\
                   "detail TEXT,"\
                   "remarks TEXT,"\
                   "tag_id TEXT,"\
                   "create_date TEXT,"\
                   "update_date TEXT,"\
                   "dead_line TEXT,"\
                   "complate_date TEXT,"\
                   "complate_flag INTEGER,"\
                   "frozen_flag INTEGER,"\
                   "priority_rank INTEGER"\
                   ")"