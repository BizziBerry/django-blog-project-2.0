from django.test import TestCase, Client
from django.urls import reverse
from .models import Post
from django.utils import timezone

class BlogTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(
            title='Тестовый пост',
            content='Тестовое содержание',
            created_at=timezone.now()
        )
    
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
    
    def test_post_list_page_status_code(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_post_detail_page_status_code(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
    
    def test_post_create_page_status_code(self):
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 200)
    
    def test_post_creation(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'Новый пост',
            'content': 'Содержание нового поста'
        })
        self.assertEqual(response.status_code, 302)  # redirect after success
        self.assertTrue(Post.objects.filter(title='Новый пост').exists())
    
    def test_post_edit_page_status_code(self):
        response = self.client.get(reverse('post_edit', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
    
    def test_post_delete_page_status_code(self):
        response = self.client.get(reverse('post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
