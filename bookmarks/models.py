from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Bookmark(models.Model):
    """
    Bookmark model which is related to 'owner' and 'post' model.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='bookmark',
                             on_delete=models.CASCADE
                             )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
