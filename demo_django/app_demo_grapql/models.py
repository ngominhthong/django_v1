from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.

class User(AbstractUser):
    avatar=models.ImageField(upload_to='static/upload/user/%Y/%m')
    

class Content(models.Model):
    class Meta:
        abstract=True
    title=models.CharField(max_length=250,null=True,blank=True)
    show=models.BooleanField(default=True)
    active=models.BooleanField(default=True)
    def __str__(self) :
        return str(self.id) +" : "+ self.title

class Page(Content):
    styte=models.CharField(max_length=250,null=True,blank=True)

class Layout_catergory(models.Model):
    styte=models.CharField(max_length=250,null=False,unique=True)
    groud=models.CharField(max_length=250,null=False,blank=True)
    def __str__(self) :
        return self.styte

class Layout(Content):
    class Meta:
        ordering=["parent","priority"]
    priority=models.CharField(max_length=250,null=False,unique=True)
    name=models.CharField(max_length=250,null=True,blank=True)
    dest=RichTextField()
    styte=models.TextField(null=True,blank=True)
    parent=models.CharField(max_length=255,null=True,blank=True)
    catergory=models.ForeignKey(Layout_catergory,on_delete=models.SET_NULL,null=True,blank=True)
    page=models.ForeignKey(Page,on_delete=models.CASCADE,default=1)

class Layout_img(Content):
    layout=models.ForeignKey(Layout,on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to='static/upload/Layout_img/%Y/%m')
    name=models.CharField(max_length=250,null=True,blank=True)
    dest=RichTextField(null=True)
    def __str__(self) :
        return self.title

class Catergory(Content):
    class Meta:
        unique_together=['title']
    parent=models.CharField(max_length=250,null=True,blank=True)
    avatar=models.ImageField(upload_to='static/upload/Catergory/%Y/%m',null=True,blank=True)
  

class Menu(Content):
    class Meta:
        unique_together=['title']
        ordering=["parent","priority"]
    priority=models.CharField(max_length=250,null=True,blank=True)
    parent=models.CharField(max_length=250,null=True,blank=True)
    #url=models.CharField(max_length=250,null=False)
    page=models.ForeignKey(Page,on_delete=models.SET_DEFAULT,null=True,default="")
    avatar=models.ImageField(upload_to='static/upload/Menu/%Y/%m')

class Item(Content):
    class Meta:
        unique_together=['title']
        ordering=["created_date"]
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
    avatar=models.ImageField(upload_to='static/upload/Item/%Y/%m')
    prite=models.CharField(max_length=250,null=False)
    prite_promotion=models.CharField(max_length=250,null=False)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    dest=RichTextField(null=True)
    

class tag_catergory(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    catergory=models.ForeignKey(Catergory,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)