from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    book_content_type = ContentType.objects.get(app_label='bookshelf', model='Book')

    # Permissions
    permissions = {
        "can_view": Permission.objects.get(codename="can_view", content_type=book_content_type),
        "can_create": Permission.objects.get(codename="can_create", content_type=book_content_type),
        "can_edit": Permission.objects.get(codename="can_edit", content_type=book_content_type),
        "can_delete": Permission.objects.get(codename="can_delete", content_type=book_content_type),
    }

    # Groups
    groups = {
        "Editors": ["can_view", "can_create", "can_edit"],
        "Viewers": ["can_view"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    }

    for group_name, perms in groups.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm in perms:
            group.permissions.add(permissions[perm])

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "date_of_birth", "password1", "password2", "is_staff", "is_active"),
        }),
    )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

