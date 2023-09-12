from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

from utils.validators import validate_sku

class Package(models.Model):
    title = models.CharField(_('title') , max_length=50)
    sku = models.CharField(_('stock keeping only'),max_length=20 , validators=[validate_sku] ,db_index=True)
    description = models.TextField(_('description') , blank =True)
    avatar = models.ImageField(_('avatar') , blank=True , upload_to='packages/')
    is_enable = models.BooleanField(_('is_enable') , default=True)
    price = models.PositiveIntegerField(_('price'))
    duration = models.DurationField(_('duration') , blank=True , null=True)
    created_time = models.DateTimeField(_('created_time') , auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time') , auto_now=True)


    class Meta:
        db_table = 'packages'
        verbose_name = _('Package')
        verbose_name_plural = _('Packages')


    def __str__(self):
        return self.title

class Subscription(models.Model):
    user = models.ForeignKey('users.User' , related_name='%(class)s' , on_delete=models.CASCADE)
    package = models.ForeignKey(Package , related_name='%(class)s' , on_delete=models.CASCADE)
    created_time = models.DateTimeField(_('created_time') , auto_now_add=True)
    expire_time = models.DateTimeField(_('expire_time') , blank=True , null=True)

    class Meta:
        db_table = 'subscriptions'
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')