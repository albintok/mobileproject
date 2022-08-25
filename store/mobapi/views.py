from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from mobapi.models import Bikes
from mobapi.serializers import BikeSerializer


class BikeView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Bikes.objects.all()
        if "colour" in request.query_params:
            qs=qs.filter(colour=request.query_params.get("colour"))
        if "name" in request.query_params:
            qs=qs.filter(name__contains=request.query_params.get("name"))
        serilaizer=BikeSerializer(qs,many=True)
        return Response(data=serilaizer.data)

    def post(self,request,*args,**kwargs):
        serializer=BikeSerializer(data=request.data)
        if serializer.is_valid():
            Bikes.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class BikeDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Bikes.objects.get(id=id)
        serializer=BikeSerializer(qs)
        return Response(data=serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Bikes.objects.get(id=id)
        qs.delete()
        return Response({"msg":"deleted"})
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Bikes.objects.filter(id=id)
        serilizer=BikeSerializer(instance=qs,data=request.data)
        if serilizer.is_valid():
            # qs.name=serilizer.validated_data.get("name")
            # qs.colour=serilizer.validated_data.get("colour")
            # qs.cc=serilizer.validated_data.get("cc")
            # qs.price=serilizer.validated_data.get("price")
            # qs.brand=serilizer.validated_data.get("brand")
            # qs.save()
            qs.update(**serilizer.validated_data)
            return Response({"msg":"updated"})
        else:
            return Response(data=serilizer.errors)


# Create your views here.
