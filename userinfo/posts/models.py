from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils import timezone
from settings.models import Settings
from django.contrib.auth.models import User
from datetime import datetime

class Posts(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title = models.CharField("Title", max_length=25, default="title", null=True)
    description = models.CharField("Description", max_length=100, default="Description", null=True)
    # is_authenticated = models.BooleanField("Is Authenticated")
    rating = models.IntegerField("Rating", null=True)
    place = models.CharField( "Place",max_length=20 ,default="Place1", null=True)
    image = models.ImageField(upload_to='post_images')
    # created=models.DateTimeField(default=datetime.today, null=True)
    # updated=models.DateTimeField(auto_now=True, null=True)
    # slug=models.SlugField(max_length=264, unique_for_date='publish', null=True)
    # setting_id=models.ForeignKey(Settings,on_delete=models.CASCADE, null=True)
    author=models.ForeignKey(User, related_name='blog_posts',on_delete=models.CASCADE, default=1)
    # body=models.TextField("Body",null=True)
    # publish=models.DateTimeField(default=timezone.now, null=True)
    # status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='draft', null=True)
    tags=TaggableManager()
    #parent_places = ChildPosts(many=True, read_only=True)

    #published posts should display in descending order of date ,latest one should come first
    # class Meta:
    #     ordering=('-publish',)

    #if we need title for that purpose we create it
    def __str__(self):
        return self.title

# class ChildPosts(models.Model):
#     description = models.CharField("Description", max_length=100, default="Description", null=True)
#     place = models.CharField("Place", max_length=20, default="Journey to The End of the World...", null=True)
#     image = models.ImageField(upload_to='post_images')
#     author = models.ForeignKey(Posts, related_name='parent_places', on_delete=models.CASCADE, default=1)
#
#
#     class Meta:
#         ordering=('-created',)
#
#
#     def __str__(self):
#         return self.place



                # def get_absolute_url(self):
    #     return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

class Comments(models.Model):
    post=models.ForeignKey(Posts,"Posts")
    name=models.CharField(max_length=32, null=True)
    email=models.EmailField("Email", null=True)
    body=models.TextField("Body", null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=('-created',)

    def __str__(self):
        return 'commented by{} on {}'.format(self.name,self.post)
