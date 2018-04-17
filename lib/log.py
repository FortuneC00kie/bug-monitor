#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-16 09:26:14
# @Author  : Fortune_c00kie (mr.chery666@gmail.com)
# @Link    : https://hacksec.xyz

import logging
import logging.handlers
from logging.handlers import TimedRotatingFileHandler
import configparser
from os import path

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
LOG_FILE = path.abspath('.') + "/log/monitor.log"

handler = TimedRotatingFileHandler(LOG_FILE, when = 'D', encoding='utf-8')
logging.basicConfig(format="%(levelname)s — %(module)s — %(asctime)s — %(message)s", level=logging.INFO,
                    handlers=[handler, ])


def debug(msg):
    logging.debug(msg)


def info(msg):
    logging.info(msg)


def warning(msg):
    logging.warning(msg)


def error(msg):
    logging.error(msg)


def critical(msg):
    logging.critical(msg)


def exception(e):
    logging.exception(e)

# test
if __name__ == '__main__':
    warning("这个是警告")
    try:
        1/0
    except Exception as e:
        exception(e)
    
