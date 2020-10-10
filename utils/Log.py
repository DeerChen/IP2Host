'''
Description: 日志封装
Author: Senkita
Date: 2020-10-09 13:34:41
LastEditors: Senkita
LastEditTime: 2020-10-09 13:56:30
'''
import logging
from logging import handlers
import os
import time


class levelFilter(logging.Filter):
    """
    description: 过滤等级
    param {type}
    return {type}
    author: Senkita
    """

    def filter(self, record):
        if record.levelno < logging.ERROR:
            return False
        return True


def _logging(**kwargs):
    """
    description: 日志封装
    param {str} level - [等级]
          {str} filename - [文件名]
          {str} datefmt - [时间格式]
          {str} format - [日志格式化]
    return {logging.Logger} logger - [日志实例]
    author: Senkita
    """

    # 参数初始化
    default_level = logging.INFO
    default_datefmt = '%Y-%m-%d %H:%M:%S'
    filename_fmt = time.strftime('%Y-%m-%d', time.localtime())
    default_filename = os.path.join(os.getcwd(), 'Log/{}.log'.format(filename_fmt))
    default_fmt = (
        '%(asctime)s-[%(name)s]-%(filename)s-[%(lineno)s] | %(levelname)s: %(message)s'
    )

    level = kwargs.pop('level', default_level)
    filename = kwargs.pop('filename', default_filename)
    datefmt = kwargs.pop('datefmt', default_datefmt)
    fmt = kwargs.pop('format', default_fmt)

    # 实例化
    logger = logging.getLogger(filename)
    # 构建格式化参数
    formatter = logging.Formatter(fmt, datefmt)

    # 输出到控制台
    sh_handler = logging.StreamHandler()

    sh_handler.addFilter(levelFilter())
    sh_handler.setFormatter(formatter)
    sh_handler.setLevel(default_level)

    '''
    # 按文件大小分隔日志
    r_file_handler = handlers.RotatingFileHandler(
        filename=filename,
        mode='a',
        maxBytes=524288,
        backupCount=5,
        encoding='utf-8',
        delay=False,
    )
    r_file_handler.setFormatter(formatter)
    r_file_handler.setLevel(default_level)
    '''

    # 按日分割日志
    tr_file_handler = handlers.TimedRotatingFileHandler(
        filename=filename, when='midnight', backupCount=7, encoding='utf-8'
    )

    # 设置file_handler的格式化参数和等级
    tr_file_handler.setFormatter(formatter)
    tr_file_handler.setLevel(default_level)

    # 添加handler
    logger.addHandler(sh_handler)
    # // logger.addHandler(r_file_handler)
    logger.addHandler(tr_file_handler)
    logger.setLevel(level)

    return logger
