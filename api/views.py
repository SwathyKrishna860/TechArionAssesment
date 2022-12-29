from django.shortcuts import render
from .models import Product,ProductColorModel,ProductImageModel
from .serializers import ProductSerializer,ProductClrSerializer,ProductImgSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class ProductView(APIView):
    def get(self,request,*args,**kwargs):
        queryset=Product.objects.all()
        serializers=ProductSerializer(queryset,many=True)
        return Response(data=serializers.data)

    def post(self,request,*args,**kwargs):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(data=serializer.errors)

class ProductClrView(APIView):
    def get(self,request,*args,**kwargs):
        queryset=ProductColorModel.objects.all()
        serializers=ProductClrSerializer(queryset,many=True)
        return Response(data=serializers.data)

    def post(self,request,*args,**kwargs):
        serializer=ProductClrSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(data=serializer.errors)

class ProductImageView(APIView):
    def get(self,request,*args,**kwargs):
        queryset=ProductImageModel.objects.all()
        serializers=ProductImgSerializer(queryset,many=True)
        return Response(data=serializers.data)

    def post(self,request,*args,**kwargs):
        serializer=ProductImgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(data=serializer.errors)


