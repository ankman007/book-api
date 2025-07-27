from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=500)
    author = serializers.CharField(max_length=255)
    published_date = serializers.DateField()
    
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()
        return instance
