from django.urls import reverse, resolve
from django.test import TestCase
from django.contrib.auth.models import User

from .. import views


class ViewsTestCase(TestCase):
    
    def setUp(self) -> None:
        self.user1 = User.objects.create_user(
            username='testuser1'
        )
        
    def test_home_view(self):
        url = reverse('home')
        function = resolve(url).func
        
        self.assertEqual(function, views.home)
       
        
    def test_search_view(self):
        url = reverse('search')
        function = resolve(url).func
        
        self.assertEqual(function, views.search)
       
        
    def test_add_view(self):
        url = reverse('add')
        function = resolve(url).func
        
        self.assertEqual(function, views.add_film)
        
        
    def test_bookmarks_view(self):
        url = reverse('bookmarks')
        function = resolve(url).func
        
        self.assertEqual(function, views.bookmarks)
        
        
    def test_film_page_view(self):
        url = reverse('film_page', args={1})
        function = resolve(url).func
        
        self.assertEqual(function, views.film_page)
        
        
    def test_streaming_view(self):
        url = reverse('stream', args={1})
        function = resolve(url).func
        
        self.assertEqual(function, views.get_streaming_video)
        

