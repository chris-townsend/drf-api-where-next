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


class PostDetailViewTests(APITestCase):
    """
    Testing PostDetail views with two test users
    """
    def setUp(self):
        chris = User.objects.create_user(
            username='chris', password='password')
        sam = User.objects.create_user(
            username='sam', password='password')
        Post.objects.create(
            owner=chris, title='test title')
        Post.objects.create(
            owner=sam, title='test title two')

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'test title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='chris', password='password')
        response = self.client.put('/posts/1/', {'title': 'test title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'test title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_edit_another_users_post(self):
        self.client.login(username='sam', password='password')
        response = self.client.put('/posts/1/', {'title': 'test title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
