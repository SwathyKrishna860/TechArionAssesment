from rest_framework import serializers
from .models import Product,ProductColorModel,ProductImageModel

class ProductSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Product
        fields=[
            "id",
            "title",
            "description",
            "price",
            "unique_code",
            "size",
            "quality",
        ]

class ProductClrSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductColorModel
        fields=[
            "product",
            "color",
        ]

class ProductImgSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImageModel
        fields=[
            "product_im",
            "image",
        ]