from django.db import models
#------------
from django.contrib.auth.models import User



class Profile(models.Model):
    """Profile model.

    Proxy model that extends the base data with other
    information.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.user.username
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class User(models.Model):
    """modelo de usuario"""

    email=models.EmailField(unique=True)
    password=models.CharField(max_length=30)

    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)

    is_admin=models.BooleanField(default=False)
    bio=models.TextField()
    birthdate=models.DateField(blank=True,null=True)

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        #print email
        return self.email
