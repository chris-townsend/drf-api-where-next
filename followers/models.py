from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model which allows users to follow eachother,
    related_name attribute used so that django can differentiate
    between 'owner' and 'followed' which are both User model instances.
    'unique_together' ensures a user can't 'double follow' the same user
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
