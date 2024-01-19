#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os


class ConfigManager(object):
    # 项目目录
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 页面元素目录
    element_path = os.path.join(base_dir, 'page_element')
    # 日志文件存放
    log_dir_path = os.path.join(base_dir, 'logs')
    # 截图
    png_path = os.path.join(base_dir, 'file', 'picture')
    # 测试结果临时存放目录
    temp_path = os.path.join(base_dir, 'temp')
    # 测试报告存放目录
    report_path = os.path.join(base_dir, 'report')
    # resource
    resource_path = os.path.join(base_dir, 'resource')
    # allure报告配置文件
    allure_env_config = os.path.join(base_dir, 'file', 'environment.properties')
    # 项目参数配置文件
    ini_file = os.path.join(base_dir, 'config', 'config.ini')


cm = ConfigManager()
if __name__ == '__main__':
    print(cm.base_dir)
