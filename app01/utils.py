import json
from django.shortcuts import HttpResponse
import datetime


'''
修复了json不能解析datetime对象的问题
'''
class DatetimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, o)

class Tool:
    err_type = {
        'param_illegal': '缺少参数或参数非法'
    }
    def __init__(self):
        self.resp = {
            'code': 0,
            'message': 'ok',
            'data': ''
        }
    def bind_and_val(self, request, struct):
        '''

        :param request: 请求的request对象
        :param struct: 需要解读出来的数据结构(就是模型类的__dict__属性)
        :return: 解读出来的数据结构
        '''
        return json.loads(request.body.decode())


    def generate_HttpResponse(self, data='', code=0,message='ok'):
        '''

        :param data: 传给前端的数据主体
        :param code: 默认为0, 正常。 1为异常。
        :param message: 异常消息
        :return:
        '''
        tmp_resp = json.loads(json.dumps(self.resp, ensure_ascii=False))
        tmp_resp['code'] = code
        tmp_resp['message'] = message
        tmp_resp['data'] = data
        # 写成content_type为这个来达到传给前端json的目的
        return HttpResponse(json.dumps(tmp_resp, ensure_ascii=False, cls=DatetimeEncoder),content_type='application/json')