#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/2 20:48
# @Author : 心蓝
import os
# 项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 项目域名
PROJECT_HOST = 'http://api.lemonban.com/futureloan'
# 接口地址
INTERFACES = {
    'register': '/member/register',
    'login': '/member/login',
    'recharge': '/member/recharge',
    'add': '/loan/add',
    'audit': '/loan/audit',
    'invest': '/member/invest'
}

# 日志配置
LOG_CONFIG = {
    'name': 'py38',
    'filename': os.path.join(BASE_DIR, 'logs/py38.log'),
    'mode': 'a',
    'encoding': 'utf-8',
    'debug': True
}

# 测试数据配置
TEST_DATA_FILE = os.path.join(BASE_DIR, 'test_data/testcases.xlsx')

# 测试报告
REPORT_CONFIG = {
    'description': '前程贷',
    'filename': 'py38期测试报告.html',
    'report_dir': os.path.join(BASE_DIR, 'reports'),
    'title': 'py38期',
    'theme': 'theme_cyan',
    '_type': 'br'
}

# 数据库配置
DB_CONFIG = {
    'host': 'api.lemonban.com',
    'user': 'future',
    'password': '123456',
    'db': 'futureloan',
    'charset': 'utf8',
    'port': 3306,
    'autocommit': True  # 自动提交事务 防止可重复读的问题
}
