from django.test import TestCase
from django.contrib.auth.models import User, Group
from .models import Book

class PermissionTestCase(TestCase):
    def setUp(self):
        self.viewer = User.objects.create_user(username="viewer", password="test123")
        viewer_group = Group.objects.get(name="Viewers")
        self.viewer.groups.add(viewer_group)

        self.book = Book.objects.create(title="Test Book", author="Author", description="Description")

    def test_view_permission(self):
        self.client.login(username="viewer", password="test123")
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)  # Viewer should access the book list