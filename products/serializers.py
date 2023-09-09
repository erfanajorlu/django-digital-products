from rest_framework import serializers

from .models import Category , Product , File

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title' , 'description' , 'avatar')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('title' , 'file')

class CategorySerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many = True)
    class Meta:
        model = Category
        fields = ('title' , 'description' , 'avatar' , 'categories')
        
        