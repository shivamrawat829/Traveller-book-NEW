from django.db import models
# from posts.models import Posts
# from rest_auth. import
from django.contrib.auth.models import User


class UserProfile(models.Model):
    profile_image = models.ImageField("Image", blank=True, null=True)
    name = models.CharField("Name", max_length=100, blank=True, null=True)
    email = models.EmailField("Email", max_length=254)
    location = models.CharField("Location", max_length=100, null=True)
    bio = models.CharField("Bio", max_length=100, null=True)
    interests = models.CharField("Interests", max_length=100, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    followers = models.IntegerField("Followers", default=0)
    no_of_posts = models.IntegerField("No of Posts", default=0)

    def __str__(self):
        return self.name
