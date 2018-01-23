#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : mr.chery (mr.chery666@gmail.com)
from werobot import WeRoBot
import yaml

with open('config.yaml', 'r') as f:
	a = f.read()
	conf = yaml.load(a)

robot = WeRoBot()

robot.config["APP_ID"] = conf['wechat']['app_id']
robot.config["APP_SECRET"] = conf['wechat']['app_secret']

client = robot.client

def send_wechat(info):
	followers_info = client.get_followers()
	followers_list = followers_info['data']['openid']
	for follower in followers_list:
		client.send_text_message(follower, info)