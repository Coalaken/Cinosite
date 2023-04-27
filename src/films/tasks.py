import logging

from config.celery import app 
from .services import change_bookmarks1, like1


logger = logging.getLogger('celery')


@app.task
def change_bookmarks_status1(username, film_name):
    try:
        change_bookmarks1(username, film_name)
    except Exception as e:
        logger.exception(e)


@app.task
def change_like_status1(username, film_liked):
    try:
        like1(username, film_liked)
    except Exception as e:
        logger.exception(e)
    
