# Django Admin Interface Setup for Book Model

## Steps to Register and Customize Book Model in Django Admin

1. **Register the Book Model**:
   - In `bookshelf/admin.py`, we registered the `Book` model using the following code:
     ```python
     from django.contrib import admin
     from .models import Book

     @admin.register(Book)
     class BookAdmin(admin.ModelAdmin):
         list_display = ('title', 'author', 'publication_year')
         search_fields = ('title', 'author')
         list_filter = ('publication_year',)
     ```

2. **Admin Interface Features**:
   - **list_display**: Shows `title`, `author`, and `publication_year` in the list view.
   - **search_fields**: Allows searching by `title` and `author`.
   - **list_filter**: Adds a filter for `publication_year`.

3. **Accessing the Admin Interface**:
   - Start the server with `python manage.py runserver` and navigate to `http://127.0.0.1:8000/admin`.
   - Log in with your superuser credentials to manage the `Book` model.
