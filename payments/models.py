from django.db import models
from django.utils.translation import gettext_lazy as _


from utils.validators import validate_phone_number


class Gateway(models.Model):
    title = models.CharField(_('title') , max_length=50)
    description = models.TextField(_('description') , blank=True)
    avatar = models.ImageField(_('avatar') , blank=True,upload_to='gateways/')
    is_enable = models.BooleanField(_('is_enable') , default=True)
    created_time = models.DateTimeField(_('created_time') , auto_now_add=True)
    updated_time = models.DateTimeField(_('updated_time') , auto_now=True)


    class Meta:
        db_table = 'Gateways'
        verbose_name = _('Gateway')
        verbose_name_plural =   _('Gateways')


class Payment(models.Model):
    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_ERROR = 20
    STATUS_CANCEL = 30
    STATUS_REFUNDED = 31
    STATUS_CHOICES = (
        (STATUS_VOID , _('Void')),
        (STATUS_PAID , _('Paid')),
        (STATUS_ERROR , _('Error')),
        (STATUS_CANCEL , _('User Canceled')),
        (STATUS_REFUNDED , _('Refunded')),
    )


    STATUS_TRANSLATION = {
        STATUS_VOID: _('Payment could not be processed'),
        STATUS_PAID: _('Payment successful'),
        STATUS_ERROR: _('Payment has encountered an error'),
        STATUS_CANCEL: _('Payment canceled by user.'),
        STATUS_REFUNDED: _('This payment has been refunded.'),
    }


    user = models.ForeignKey('users.User' , related_name='%(class)s' , on_delete=models.CASCADE)
    package = models.ForeignKey('subscriptions.Package', related_name='%(class)s' , on_delete=models.CASCADE)
    gateway = models.ForeignKey(Gateway , verbose_name=_('getway') , related_name='%(class)s' , on_delete=models.CASCADE)
    price = models.PositiveIntegerField(_('price') , default=True)
    status = models.PositiveSmallIntegerField(_('status') , choices=STATUS_CHOICES , default=STATUS_VOID)
    device_uuid = models.CharField(_('device uuid') , max_length=40 , blank=True)
    token = models.CharField(max_length=50)
    phone_number = models.BigIntegerField(_('phone number') , validators=[validate_phone_number])
    consumed_code = models.PositiveIntegerField(_('consumed refrence code') , null=True , db_index=True)
    created_time = models.DateTimeField(_('created_time') , auto_now_add=True)
    expire_time = models.DateTimeField(_('expire_time') , blank=True , null=True)


    class Meta:
        db_table = 'Payments'
        verbose_name = _('Payment')
        verbose_name_plural =   _('Payments')
