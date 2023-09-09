from django.db import models
from django.utils.translation import gettext_lazy as _ 

# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self' , verbose_name=_('parent') , blank=True , null=True , on_delete=models.CASCADE)
    title = models.CharField(_('title') , max_length=50)
    description = models.TextField(_('description') , blank=True)
    avatar = models.ImageField(_('avatar') , blank=True,upload_to='categories')
    is_enable = models.BooleanField(_('is_enable') , default=True)
    created_time = models.DateTimeField(_('created_time') , auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time') , auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural =   _('Categories')

class Product(models.Model):
    title = models.CharField(_('title') , max_length=50)
    description = models.TextField(_('description') , blank=True)
    avatar = models.ImageField(_('avatar') , upload_to='products/') 
    is_enable = models.BooleanField(_('is enable') , default=True)
    categories = models.ManyToManyField('Category' , verbose_name=_('categories') ,blank=True)
    created_time = models.DateTimeField(_('created time') , auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time') , auto_now=True)


    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural =   _('Products')

class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPES =(
        (FILE_AUDIO ,_('audio')),
        (FILE_VIDEO ,_('video')),
        (FILE_PDF ,_('pdf')),
    )

    product = models.ForeignKey('Product' ,verbose_name=_('product') ,related_name='files' ,on_delete=models.CASCADE)
    title = models.CharField(_('title') , max_length=50)
    file  = models.FileField(_('file') ,upload_to=('files/%Y/%m/%d/'))
    file_type = models.PositiveSmallIntegerField(_('file type'),choices=FILE_TYPES)
    is_enable = models.BooleanField(_('is enable') , default=True)
    created_time = models.DateTimeField(_('created time') , auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time') , auto_now=True)


    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')
