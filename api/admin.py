from django.contrib import admin
from .models import Product,ProductColorModel,ProductImageModel

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductColorModel)
admin.site.register(ProductImageModel)

