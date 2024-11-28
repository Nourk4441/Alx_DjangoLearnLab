from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend

"""
BookListView: Handles GET requests to retrieve a list of all books.
BookDetailView: Handles GET requests to retrieve details of a specific book.
BookCreateView: Handles POST requests to add a new book.
BookUpdateView: Handles PUT requests to modify an existing book.
BookDeleteView: Handles DELETE requests to remove a book.
"""

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

     # Adding filtering, searching, and ordering capabilities
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Define filter fields for DjangoFilterBackend
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Define search fields for SearchFilter
    search_fields = ['title', 'author__name']

    # Define ordering fields for OrderingFilter
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

# Example for testing:
# Filtering: /api/books/?title=SomeTitle&author__name=AuthorName
# Searching: /api/books/?search=Keyword
# Ordering: /api/books/?ordering=publication_year

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
        
