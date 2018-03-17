#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : mr.chery (mr.chery666@gmail.com)
from struts import *
from seebug import *
from cve import *
from threading import Timer


def struts_monitor():
	time = 60 *5
	struts_check()
	t = Timer(time, struts_monitor)
	t.start()

def seebug_monitor():
	time = 60 * 60 * 6
	seebug_crawer()
	t = Timer(time, seebug_monitor)
	t.start()

def cve_monitor():
	time = 60 * 60 * 6
	cve_crawer()
	t = Timer(time, cve_monitor)
	t.start()

if __name__ == '__main__':
	struts_init()
	struts_monitor()
	seebug_monitor()
	cve_monitor()