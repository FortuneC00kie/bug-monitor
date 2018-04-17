#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : mr.chery (mr.chery666@gmail.com)
from werobot import WeRoBot
import configparser
import sys


config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")

robot = WeRoBot()

robot.config["APP_ID"] = config["wechat"]["app_id"]
robot.config["APP_SECRET"] = config["wechat"]["app_secret"]

client = robot.client

def send_wechat(info):
	followers_info = client.get_followers()
	followers_list = followers_info['data']['openid']
	for follower in followers_list:
		client.send_text_message(follower, info)