from django.db import models

"""
Author: Represents an author with a name.
Book: Represents a book with a title, publication year, and an associated author.
The relationship between Author and Book is one-to-many.
"""
    
class Author(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} at {self.publication_year}"
     
    

