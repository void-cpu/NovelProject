# -*- coding: utf-8 -*-
# @Time    : 2021/2/17 下午5:02
# @Author  : void bug
# @FileName: ResponseMessage.py
# @Software: PyCharm
from enum import Enum


class ResponseMessage(Enum):
    NullMessage = '参数不完整'  # 前端传递的参数不完整
    NoteFound = '查找信息不存在不存在'  # 用户不存在/查找信息不存在

    @staticmethod
    class Code:
        CodeError = "验证错误"
        CodeSuccessful = "验证成功"

        def __init__(self, is_True):
            self.is_True = is_True

        def __str__(self):
            if self.is_True:
                return self.CodeSuccessful
            else:
                return self.CodeError
