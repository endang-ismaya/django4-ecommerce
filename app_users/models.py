from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    image = models.ImageField(default="profile.jpg", upload_to="profile_picture")
    contact_number = models.CharField(max_length=100, default="081300000000")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
