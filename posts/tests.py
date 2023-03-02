from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    """
    Testing PostList views with setUp test user
    """
    def setUp(self):
        User.objects.create_user(username='chris', password='password')

    def test_can_display_posts(self):
        chris = User.objects.get(username='chris')
        Post.objects.create(owner=chris, title='test title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_posts(self):
        self.client.login(username='chris', password='password')
        response = self.client.post('/posts/', {'title': 'test title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_create_posts(self):
        response = self.client.post('/posts/', {'title': 'test title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
