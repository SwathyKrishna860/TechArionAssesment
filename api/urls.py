
from django.urls import path,include
from .views import ProductView,ProductImageView,ProductClrView

urlpatterns = [
    path('product/',ProductView.as_view()),
    path('color/',ProductClrView.as_view()),
    path('image/',ProductImageView.as_view()),
    
]