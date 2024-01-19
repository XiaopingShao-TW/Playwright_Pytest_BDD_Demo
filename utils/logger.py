#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging
import os
from config.conf import cm
from utils.time import date_time_now


class Log:
    def __init__(self):
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

            # 创建一个handle写入文件
            log_file = os.path.join(cm.log_dir_path, '{}.log'.format(date_time_now()))
            fh = logging.FileHandler(log_file, encoding='utf-8')
            fh.setLevel(logging.INFO)

            # 创建一个handle输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 定义输出的格式
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 添加到handle
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    @property
    def fmt(self):
        return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'


log = Log().logger

if __name__ == '__main__':
    log.info('hello world')