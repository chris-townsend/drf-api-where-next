from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner' - a User instance,
    default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    about = models.TextField()
    image = models.ImageField(
        upload_to='images/', default='../default_post_twjz4m', blank=True)

    class Meta:
        """
        Return post instances in reverse order so newest is first
        """
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.id} {self.title}'
