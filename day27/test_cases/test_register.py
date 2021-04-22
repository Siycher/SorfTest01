#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/26 20:43
# @Author : 心蓝
import json
import unittest

from Python_web_UI_38.day27.test_cases.base_case import BaseTest
from Python_web_UI_38.day27 import settings
from Python_web_UI_38.day27.common.myddt import ddt, data
from Python_web_UI_38.day27.common.test_data_handler import get_test_data_from_excel


# 从excel中提取用例数据
cases = get_test_data_from_excel(settings.TEST_DATA_FILE, 'register')


@ddt
class TestRegister(BaseTest):
    name = '注册'

    @data(*cases)
    def test_register(self, case):
        self.checkout(case)


if __name__ == '__main__':
    unittest.main()