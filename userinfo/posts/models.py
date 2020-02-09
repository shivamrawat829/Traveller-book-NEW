from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils import timezone
from user_profile.models import UserProfile
from django.contrib.auth.models import User
from datetime import datetime


class Posts(models.Model):
    title = models.CharField("Title", max_length=25, default="title", null=True)
    description = models.TextField("Description", max_length=1200, default="Description", null=True)
    rating = models.IntegerField("Rating", null=True)
    place = models.CharField("Place", max_length=20, default="Place", null=True)
    image = models.ImageField(upload_to='media')
    created = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=264, null=True)
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE, default=1)
    tags = TaggableManager()
    city = models.CharField("City", max_length=20, default="Delhi")
    # liked = models.ImageField("Liked", default=0)
    #published posts should display in descending order of date ,latest one should come first
    # class Meta:
    #     ordering=('-publish',)

    def __str__(self):
        return self.title


class Places(models.Model):
    place = models.CharField("Place", max_length=50, default="Journey to The End of the World...", null=True)
    description = models.CharField("Description", max_length=1200, default="Good place...", null=True)
    image = models.ImageField(upload_to='media')
    post_id = models.ForeignKey(Posts, related_name='places', on_delete=models.CASCADE, default=1)
    # user_id = models.ForeignKey(User, related_name='blog_posts',on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ('-place',)

    def __str__(self):
        return self.place
                # def get_absolute_url(self):
    #return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])


class Comments(models.Model):
    post = models.ForeignKey(Posts, related_name='post_id', on_delete=models.CASCADE, default=1)
    comment = models.TextField(max_length=32, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'commented by{} on {}'.format(self.comment, self.post)
