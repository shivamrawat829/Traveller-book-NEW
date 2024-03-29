# Generated by Django 2.2.3 on 2020-02-09 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=25, null=True, verbose_name='Title')),
                ('description', models.TextField(default='Description', max_length=1200, null=True, verbose_name='Description')),
                ('rating', models.IntegerField(null=True, verbose_name='Rating')),
                ('place', models.CharField(default='Place', max_length=20, null=True, verbose_name='Place')),
                ('image', models.ImageField(upload_to='media')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(max_length=264, null=True)),
                ('city', models.CharField(default='Delhi', max_length=20, verbose_name='City')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(default='Journey to The End of the World...', max_length=50, null=True, verbose_name='Place')),
                ('description', models.CharField(default='Good place...', max_length=1200, null=True, verbose_name='Description')),
                ('image', models.ImageField(upload_to='media')),
                ('post_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='places', to='posts.Posts')),
            ],
            options={
                'ordering': ('-place',),
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked_by_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=32, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_id', to='posts.Posts')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
