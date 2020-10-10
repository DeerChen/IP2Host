'''
Description: 进度条
Author: Senkita
Date: 2020-10-09 13:59:58
LastEditors: Senkita
LastEditTime: 2020-10-09 14:05:32
'''
import sys
import math


def progress_bar(portion, total):
    """
    description: 进度条
    param {int} portion - [已完成量]
          {int} total - [总量]
    return {bool} 是否完成
    author: Senkita
    """
    # 一小块大小
    part = total / 50
    count = math.ceil(portion / part)
    sys.stdout.write('\r')
    sys.stdout.write(('[%-50s]%.2f%%' % (('>' * count), portion / total * 100)))
    sys.stdout.flush()

    if portion >= total:
        sys.stdout.write('\n')
        return True
