#!/usr/bin/env python
#-*-coding: utf-8-*-

from logging import config
from logging import getLogger
import datetime
import json
import os



with open (os.path.join(os.path.dirname(__file__),"../conf/log_config.json")) as f:
    log_name = os.path.join(os.path.dirname(__file__),"../logs/" + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + ".log")
    print(log_name)
    log_conf = json.load(f)
    log_conf['handlers']['logFileHandler']['filename']=log_name
    config.dictConfig(log_conf)

def org_get_logger(logger_name):
    return getLogger(logger_name)