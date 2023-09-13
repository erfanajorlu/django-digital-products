from rest_framework import serializers


from .models import Package , Subscription

class PackageSerializer(serializers.ModelSerializer):
    class meta:
        model = Package
        fields = ('title' , 'sku', 'description' , 'avatar' , 'price' , 'duration')

class SubscriptionSerializer(serializers.ModelSerializer):
    package = PackageSerializer()

    class Meta:
        model = Subscription
        fields = ('package' , 'created_time' , 'expire_time')