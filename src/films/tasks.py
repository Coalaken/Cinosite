import time

from config.celery import app 
from .services import change_bookmarks1, like1


@app.task
def change_bookmarks_status1(username, film_name):
    change_bookmarks1(username, film_name)


@app.task
def change_like_status1(username, film_liked):
    like1(username, film_liked)
    
