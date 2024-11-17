from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookSearchForm

def search_books(request):
    form = BookSearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)
    else:
        books = []
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Handle book editing logic
    return render(request, 'bookshelf/edit_book.html', {'book': book})

def index(request): return HttpResponse("Welcome to my book store.")