#!/usr/bin/env python
#-*-coding: utf-8-*-

from todo_manager import app
from todo_manager.lib.log import org_get_logger


if __name__ == "__main__":
    logger = org_get_logger(__name__)
    logger.info("__startup__")
    app.run()
    