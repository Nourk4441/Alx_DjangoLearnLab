from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self',symmetrical=False,related_name='follower')
    following = models.ManyToManyField('self',symmetrical=False,related_name='followingg')

# Add related_name to avoid reverse accessor clashes
    groups = models.ManyToManyField(
        Group,
        related_name="groups_set", 
        blank=True,
        help_text="The groups this user belongs to.",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="permissions_set", 
        blank=True,
        help_text="Specific permissions for this user.",
    )    
