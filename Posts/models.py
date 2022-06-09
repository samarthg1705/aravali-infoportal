from django.db import models
from django.urls import reverse


# import Posts.views as post_view


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name="Name")

    def __str__(self):
        return self.name


class Post(models.Model):
    forum = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Forum")
    title = models.CharField(max_length=200, verbose_name="Title")
    image = models.ImageField(blank=True, null=True, verbose_name="Image")
    body = models.TextField(verbose_name="Body")
    author = models.CharField(max_length=40, verbose_name="Author")
    modified = models.DateTimeField(auto_now_add=True, verbose_name="Date Modified")
    created = models.DateTimeField(auto_now=False, verbose_name="Date Created")
    publish = models.BooleanField(default=True, verbose_name="Publish")
    slug = models.SlugField(max_length=200, unique=True,
                            verbose_name="Slug/Link",
                            null=True)  # For future use if individual pages for posts are created
    send_mail = models.BooleanField(default=False, verbose_name="Send Mail")  # For future use with mailing list

    def get_absolute_url(self):
        return reverse('curpost', kwargs={'slug_link': self.slug})

    def __str__(self):
        return self.title
