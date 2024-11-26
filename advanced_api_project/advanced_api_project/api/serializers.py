from rest_framework import serializers
from .models import Book, Author
from datetime import date

"""
BookSerializer: Serializes all fields of the Book model. Validates that publication_year is not in the future.
AuthorSerializer: Serializes the name field and dynamically includes all related books using a nested BookSerializer.
"""

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self,value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name','books']  
        books = BookSerializer(many=True,read_only=True)      