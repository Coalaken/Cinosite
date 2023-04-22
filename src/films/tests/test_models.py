from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


from ..models import Film, UserFilmRelation


class ModelTestCase(TestCase):
    
    def setUp(self) -> None:
        self.user1 = User.objects.create_user(
            username="testuser1"
        )
        self.user2 = User.objects.create_user(
            username="testuser2"
        )
        
        self.film1 = Film.objects.create(
            name='testname1',
            description="a description here",
            author='a author',
            added_by=self.user1
        )
        
        self.film2 = Film.objects.create(
            name='testname2',
            description="a description here",
            author='a author',
            added_by=self.user2
        )
        self.film1.viewers.add(self.user1, self.user2)
        
        self.relation = UserFilmRelation.objects.create(
            user=self.user1,
            film=self.film1,
            in_bookmarks=True,
            like=False,
            rate=3
        )
        
    def test_film_fields(self):
        film = Film.objects.first()
        
        self.assertEqual(film.name, 'testname1')
        self.assertEqual(film.description, 'a description here')
        self.assertEqual(film.author, 'a author')
        self.assertEqual(film.added_by, self.user1)
        self.assertEqual(film.viewers.count(), 3)
        
        self.assertEqual(Film.objects.all().count(), 2)
        
        
    def test_relation(self):
        relation = self.relation

        self.assertEqual(relation.user, self.user1)
        self.assertEqual(relation.film, self.film1)
        self.assertEqual(relation.in_bookmarks, True)
        self.assertEqual(relation.like, False)
        self.assertEqual(relation.rate, 3)
        
        
    def test_users(self):
        user_relation_films = self.user1.films.all()

        self.assertEqual(user_relation_films.count(), 2)