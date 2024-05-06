from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import user
from .serializers import details
from django.shortcuts import get_object_or_404


class MyApiView(APIView):
    def post(self,request):
        mydata=details(data=request.data)
        if mydata.is_valid():
            mydata.save()
            return Response({"status":'success','data':mydata.data})
        else:
            return Response({'status':'error','data':mydata.errors})

    def get(self, request,id=None, *args, **kwargs):
        if id is not None:
            result=user.objects.get(id=id)
            mydata=details(result)
            return Response({'status':'success','data':mydata.data})
        result=user.objects.all()
        mydata=details(result,many=True)
        return Response({'status':'success','data':mydata.data})
    def delete(self,request,id):
        mydata=get_object_or_404(user,id=id)
        mydata.delete()
        return Response({'status':'success','data':'Record Delete'})
    def put(self,request,id):
        data1=get_object_or_404(user,id=id)
        mydata=details(data1,data=request.data)
        if mydata.is_valid():
            mydata.save()
            return Response({"status":'success','data':mydata.data})
        else:
            return Response({'status':'error','data':mydata.errors})
    def patch(self,request,id):
        data1=get_object_or_404(user,id=id)
        mydata=details(data1,data=request.data,partial=True)
        if mydata.is_valid():
            mydata.save()
            return Response({"status":'success','data':mydata.data})
        else:
            return Response({'status':'error','data':mydata.errors})
    
        


    

        

