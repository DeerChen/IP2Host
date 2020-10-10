'''
Description: 自定义异常类
Author: Senkita
Date: 2020-10-09 13:33:52
LastEditors: Senkita
LastEditTime: 2020-10-09 13:34:02
'''


class Error(Exception):
    """
    description:自定义异常类
    param {str} err - [异常信息]
    return {type}
    author: Senkita
    """

    def __init__(self, err):
        self.error = err

    def __repr__(self):
        return self.error
