from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    """
    Group model to organize users into groups,
    related to 'owner' - a User instance.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(
        User, related_name='group_members', blank=True)

    class Meta:
        ordering = ['-created_date']
        unique_together = ('owner', 'group_name')

    def __str__(self):
        return f'{self.group_name} {self.owner}'
