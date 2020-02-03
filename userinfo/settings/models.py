from django.db import models
# from posts.models import Posts
# from rest_auth. import 
from django.contrib.auth.models import User


class Settings(models.Model):
    profile_image = models.ImageField("Image", blank=True, null=True)
    name = models.CharField("Name", max_length=100, blank=True, null=True)
    email = models.EmailField("Email", max_length=254)
    location = models.CharField("Location",max_length=100, null=True)
    bio = models.CharField("Bio",max_length=100, null=True)
    interests = models.CharField("Interests",max_length=100, null=True)
    # comment = models.CharField("Comment", max_length=100, default="Comment1")
    # is_authenticated = models.BooleanField("Is Authenticated")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name