from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    unique_code=models.CharField(max_length=50,unique=True)
    
    soptions=(
        ("10","10"),
        ("20","20"),
        ("30","30"),
    )

    size=models.CharField(max_length=50,choices=soptions)

    qoptions=(
        ("high","high"),
        ("low","low"),
        ("medium","medium"),
    )

    quality=models.CharField(max_length=50,choices=qoptions)

    def __str__(self):
        return self.title

class ProductColorModel(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    
    clr_options=(
        ("red","red"),
        ("blue","blue"),
        ("green","grgit een"),
        ("black","black"),
    )
    
    color=models.CharField(max_length=100,choices=clr_options)
    def __str__(self):
        return self.color

class ProductImageModel(models.Model):
    product_im=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="img",null=True)
        