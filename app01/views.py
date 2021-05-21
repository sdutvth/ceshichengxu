from django.views import View
from app01 import utils
tool = utils.Tool()
class PermCRUD(View):

    def get(self,request):
        # 查
        user_list = [1,2,3,4,5]
        return tool.generate_HttpResponse(data=user_list)

    def post(self,request):
        # 改
        return tool.generate_HttpResponse(code=0)

    def put(self,request):
        # 增
        return tool.generate_HttpResponse(code=0)

    def delete(self,request):
        # 删
        return tool.generate_HttpResponse(code=0)