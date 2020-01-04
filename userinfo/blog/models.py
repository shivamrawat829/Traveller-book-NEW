from django.db import models
from django.contrib.auth.models import User #Import because we need User Model
from django.utils import timezone #import because we need timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=264, unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_post' ,on_delete=models.CASCADE)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    #published posts should display in descending order of date ,latest one should come first
    class Meta:
        ordering=('-publish',)

    #if we need title for that purpose we create it
    def __str__(self):
        return self.title

    @property
    def posts(self):
        return Post.objects.all()

    # def get_absolute_url(self):
        # return reverse("post_list", kwargs={'pk':self.pk,'slug':self.slug})

