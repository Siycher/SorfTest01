#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/4/16 20:51
# @Author : 心蓝
from Python_web_UI_38.day27.test_cases.base_case import BaseTest
from Python_web_UI_38.day27.common.myddt import ddt, data
from Python_web_UI_38.day27.common.test_data_handler import get_test_data_from_excel


cases = get_test_data_from_excel(BaseTest.settings.TEST_DATA_FILE, 'invest_flow')


@ddt
class TestInvestFlow(BaseTest):
    name = '投资业务流'

    @data(*cases)
    def test_invest_flow(self, case):
        self.checkout(case)