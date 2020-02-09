from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE, related_name='user_profile')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    followers = models.IntegerField('Followers', default=0)
    cover_pic = models.ImageField(default='default.jpg', upload_to='cover_pics')

    def __str__(self):
        # return f'{self.user.username} Profile'
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Followers(models.Model):
    # follower = models.OneToOneField(User,  on_delete=models.CASCADE, related_name='follower')
    follower = models.ForeignKey(User, related_name='follower_id', on_delete=models.CASCADE, null=True)
    # following = models.OneToOneField(User,  on_delete=models.CASCADE, related_name='followers')
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # followers = models.IntegerField('Followers', default=0)
    # cover_pic = models.ImageField(default='default.jpg', upload_to='cover_pics')