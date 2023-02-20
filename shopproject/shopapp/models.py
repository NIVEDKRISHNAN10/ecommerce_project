from django.db import models
from django.urls import reverse

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    img=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'


    def __str__(self):
        return '{}'.format(self.name)
    def get_url(self):
        return reverse('shopapp:products_by_category',args=[self.slug])



class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    img=models.ImageField(upload_to='product',blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return '{}'.format(self.name)
    def get_url(self):
        return reverse('shopapp:prodcatdetails',args=[self.category.slug,self.slug])