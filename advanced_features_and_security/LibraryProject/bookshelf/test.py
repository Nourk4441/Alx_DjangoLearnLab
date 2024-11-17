from django.test import TestCase
# import os
# import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'D:\\Alx_DjangoLearnLab\\advanced_features_and_security\\LibraryProject\\LibraryProject\\settings.py')
# django.setup()
from bookshelf.models import Book
from django.contrib.auth.models import User, Group


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