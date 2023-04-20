from django.db import models
from django.contrib.auth.models import User
    
    
class Film(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/', null=True)
    video = models.FileField(upload_to='videos/', null=True)
    viewers = models.ManyToManyField(User, through="UserFilmRelation", 
                                     related_name="films")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    
class UserFilmRelation(models.Model):
    DEFAULT_LIKE_TRUE = "like"
    DEFAULT_LIKE_FALSE = "No"
    
    DEFAULT_IN_BOOKMARKS = "Yes"
    DEFAULT_NOT_IN_BOOKMARKS = "No"
    
    
    
    RATE_CHOICES = (
        (1, "Ok"),
        (2, "Fine"),
        (3, "Good"),
        (4, "Nice"),
        (5, "Wow")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    in_bookmarks = models.BooleanField(default=False)
    like = models.BooleanField(default=False)
    rate = models.PositiveIntegerField(choices=RATE_CHOICES, null=True)
    
    def __str__(self) -> str:
        return f"{self.user}: {self.film.name} rate: {self.rate if self.rate else None} | \
            like: {self.DEFAULT_LIKE_TRUE if self.like else self.DEFAULT_LIKE_FALSE} | \
            in bookmarks: {self.DEFAULT_IN_BOOKMARKS if self.in_bookmarks else self.DEFAULT_NOT_IN_BOOKMARKS}"