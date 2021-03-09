# -*- coding: utf-8 -*-
# @Time    : 2021/2/17 下午4:59
# @Author  : void bug
# @FileName: Response.py
# @Software: PyCharm


class BaseResponse:
    def __init__(self, Message, Phone=str(None)):
        self.Message = Message
        self.Phone = Phone

    def __str__(self):
        if len(self.Phone) == 0:
            return dict({'Message': self.Message})
        elif len(self.Phone) > 0:
            return dict({'Message': self.Message, "phone": self.Phone})
        else:
            return None
