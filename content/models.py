from django.db import models
from django.db import models
import uuid
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
# Create your models here.

"""
Model for Contect Page Here category is mandatory

"""
class Content(models.Model):
    contentId = models.UUIDField(default=uuid.uuid4,editable=False,null=False,blank=False)
    name=models.CharField(max_length=120)
    releaseDate= models.DateTimeField(auto_now=False, auto_now_add=False)
    genre= models.CharField(max_length=120,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    category= models.CharField(max_length=500,null=False,blank=False)
    geoRights=models.CharField(max_length=500,null=True,blank=True)
    price=models.DecimalField(decimal_places=3,max_digits=1000,null=True,blank=True)
    currency=models.CharField(max_length=500,null=True,blank=True)
    slug=models.SlugField(null=True,blank=True)
    
    def __str__(self):
        return self.name
   
    @property
    def title(self):
       return self.name

   
def rl_pre_save_receiver(sender,instance,*args,**kwargs):
    instance.category=instance.category.capitalize()
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver,sender=Content )
