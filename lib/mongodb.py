#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : mr.chery (mr.chery666@gmail.com)


from pymongo import MongoClient
import datetime
from dateutil.relativedelta import relativedelta

def conn_mongo():
    conn = MongoClient('127.0.0.1', 27017)
    db = conn.mydb
    return db


def bug_info_save(name, rate, affected, info, cveid, url, addtime):
    db = conn_mongo()
    database = db.bugdata
    data = {
        'name': name,
        'rate': rate,
        'affected': affected,
        'info': info,
        'cveid': cveid,
        'url' : url,
        'addtime': addtime,
    }
    database.insert(data)
    bug_early_clean()


def bug_info_search(name):
    db = conn_mongo()
    database = db.bugdata
    return database.find_one({"name": name})


def cve_info_save(name, cveid, url,addtime):
    db = conn_mongo()
    database = db.bugdata
    data = {
        'name': name,
        'cveid': cveid,
        'url' : url,
        'addtime': addtime,
    }
    database.insert(data)
    bug_early_clean()


def cve_info_search(cveid):
    db = conn_mongo()
    database = db.bugdata
    return database.find_one({"cveid": cveid})

def bug_early_clean():
    db = conn_mongo()
    database = db.bugdata
    before_data = datetime.date.today() - relativedelta(months=+1)
    early = before_data.strftime("%Y-%m-%d")
    database.remove({"addtime":{"$lt":early}})
