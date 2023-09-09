from rest_framework import serializers

from .models import Category , Product , File

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title' , 'description' , 'avatar')

class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ('title' , 'file')
    
    def get_file_type(self,obj):
        return obj.get_file_type_display()

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many = True)
    files = FileSerializer(many=True)

    class Meta:
        model = Category
        fields = ('title' , 'description' , 'avatar' , 'categories' , 'files')