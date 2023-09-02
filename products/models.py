from django.db import models
from django.utils.translation import ugettext_lazy as _ 

# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self' , verbose_name=_('parent') , blank=True , null=True , on_delete=models.CASCADE)
    title = models.CharField(_('title') , max_length=50)
    description = models.TextField(_('description') , blank=True)
    avatar = models.ImageField(_('avatar') , upload_to='categories')
    is_enable = models.BooleanField(_('is_enable') , default=True)
    created_time = models.DateTimeField(_('created_time') , auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time') , auto_now=True)

class Product(models.Model):
    categories = models.ManyToManyField('Category' , verbose_name=_('categories') ,blank=True)
    title = models.CharField(_('title') , max_length=50)
    description = models.TextField(_('description') , blank=True)
    avatar = models.ImageField(_('avatar') , upload_to='products/') 
    is_enable = models.BooleanField(_('is enable') , default=True)
    created_time = models.DateTimeField(_('created time') , auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time') , auto_now=True)

class File(models.Model):
    product = models.ForeignKey('Product' ,verbose_name=_('product') , on_delete=models.CASCADE)
    title = models.CharField(_('title') , max_length=50)
    file  = models.FileField(_('file') ,upload_to=('files/%Y/%m/%d/'))
    is_enable = models.BooleanField(_('is enable') , default=True)
    created_time = models.DateTimeField(_('created time') , auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time') , auto_now=True)
