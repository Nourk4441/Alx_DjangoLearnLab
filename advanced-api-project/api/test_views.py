from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author

class BookAPITestCase(TestCase):
    def setUp(self):
        # Initialize the APIClient
        self.client = APIClient()

        # Create an Author instance
        self.author = Author.objects.create(name="John Doe")

        # Create a Book instance
        self.book = Book.objects.create(
            title="Sample Book",
            publication_date="2024-01-01",
            author=self.author
        )

        # Define API endpoints
        self.book_list_url = "/api/books/"
        self.book_detail_url = f"/api/books/{self.book.id}/"

    def test_create_book(self):
        # Test data
        data = {
            "title": "New Book",
            "publication_date": "2024-12-01",
            "author": self.author.id
        }

        # Make POST request
        response = self.client.post(self.book_list_url, data, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

    def test_retrieve_book(self):
        # Make GET request
        response = self.client.get(self.book_detail_url, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        # Test data
        data = {
            "title": "Updated Book",
            "publication_date": "2024-11-30",
            "author": self.author.id
        }

        # Make PUT request
        response = self.client.put(self.book_detail_url, data, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])

    def test_delete_book(self):
        # Make DELETE request
        response = self.client.delete(self.book_detail_url, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books(self):
        # Add another book
        Book.objects.create(
            title="Another Book",
            publication_date="2024-02-01",
            author=self.author
        )

        # Make GET request with filter
        response = self.client.get(f"{self.book_list_url}?title=Another", format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Another Book")

    def test_search_books(self):
        # Make GET request with search
        response = self.client.get(f"{self.book_list_url}?search=Sample", format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Sample Book")

    def test_order_books(self):
        # Add another book
        Book.objects.create(
            title="Another Book",
            publication_date="2023-12-01",
            author=self.author
        )

        # Make GET request with ordering
        response = self.client.get(f"{self.book_list_url}?ordering=publication_date", format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Another Book")

    def test_permissions(self):
        # Ensure unauthenticated users cannot create books
        self.client.login()
        data = {
            "title": "authorized Book",
            "publication_date": "2024-12-01",
            "author": self.author.id
        }
        response = self.client.post(self.book_list_url, data, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
