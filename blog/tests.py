from django.test import TestCase, Client
from blog.models import Post, Author, User
from django.utils import timezone
from django.urls import reverse
from blog.forms import PostForm

# Create your tests here.

# model test
class PostTest(TestCase):
    def user(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='password'
        )
        self.author = Author.objects.create(user=self.user)
        return self.author

        self.post = Post.objects.create(title='title', author=self.author, body='body of title', timestamp=timezone.now())
        return self.post
        print(self.post)

    def test_string_representation(self):
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)


    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'title')
        self.assertEqual(f'{self.post.author}', 'testauthor')
        self.assertEqual(f'{self.post.body}', 'body of title')

    # def test_post_creation(self):
    #     p = self.user()
    #     self.assertTrue(isinstance(p, Post))

    # def test_post_list_view(self):
    #     response = self.client.get(reverse('none'))
    #     self.assertEqual(response.status_code, 200),
    #     self.assertContains(response, 'nice body')
    #     self.assertTemplateUsed(response, 'home.html')

    # def test_post_detail_view(self):
    #     response = self.client.get('/post/1/')
    #     no_response = self.client.get('/post/500/')
    #     self.assertEqual(response.status_code, 200),
    #     self.assertEqual(no_response.status_code, 404),
    #     self.assertContains(response, 'nice body')
    #     self.assertTemplateUsed(response, 'post_detail.html')