import logging

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import StreamingHttpResponse
from django.views.generic import CreateView
from django.db.models import Count, When, Case

from .models import Film, Category
from .forms import FilmAddForm
from .services import open_file
from .tasks import change_bookmarks_status1, change_like_status1


# logger name from settings 
logger = logging.getLogger('django')


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@login_required(login_url="/login")
def home(request):
       
    if request.method == 'POST' and is_ajax(request):
        film_name = request.POST.get('button_value')      


        if film_name:
            try:
                change_bookmarks_status1.delay(request.user.username, film_name)
            # change_bookmarks_status.delay(request, Film, UserFilmRelation, film_name)
            except Exception as e:
                logger.exception(e)


    films = Film.objects.select_related('added_by').all()
    catgories = Category.objects.all()
    data = {
        'catgories': catgories,
        'films': films
    }
    return render(request, 'films/home.html', data)
    
    
@login_required(login_url="/login")
def search(request):    
    if request.method == 'POST' and is_ajax(request):
        try:
            film_name = request.POST.get("button_value")
            change_bookmarks_status1.delay(request.user.username, film_name)
        except Exception as e:
                logger.exception(e)
    try:
        search_name = request.GET.get("search")      
        films = Film.objects.select_related('added_by').\
        filter(name__icontains=search_name)
    except Exception as e:
        logger.exception(e)
    catgories = Category.objects.all()
    data = {
        'catgories': catgories,
        'films': films
    }
    return render(request, 'films/home.html', data)
    

class FilmCreateView(CreateView):
    template_name = 'films/add_film.html'
    form_class = FilmAddForm

        
        
@login_required(login_url='/login') 
def bookmarks(request):
    if request.method == 'POST' and is_ajax(request):
        try:
            film_name = request.POST.get("button_value")
            change_bookmarks_status1.delay(request.user.username, film_name)
        except Exception as e:
                logger.exception(e)
            
    films = Film.objects.select_related('added_by').\
        filter(userfilmrelation__user=request.user, userfilmrelation__in_bookmarks=True)
    catgories = Category.objects.all()
    data = {
        'catgories': catgories,
        'films': films
    }
    return render(request, 'films/home.html', data)


@login_required(login_url="/login")
def film_page(request, pk: int):
    if request.method == 'POST' and is_ajax(request):
        try:
            film_liked = request.POST.get("liked_film")
            if film_liked:
                change_like_status1.delay(request.user.username, film_liked)
        except Exception as e:
            logger.exception(e)
           
    film = Film.objects.filter(pk=pk).annotate(
        annotated_likes=(
            Count(Case(When(userfilmrelation__like=True, then=1)))
        )
    ).first()
    catgories = Category.objects.all().annotate(     
    )
    data = {
        'film': film,
        'catgories': catgories,
    }
    return render(request, 'films/film_page.html', data)


def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, Film, pk)
    response = StreamingHttpResponse(file, status=status_code,
                                     content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response


def by_category(request, pk: int):
    try:
        films = Film.objects.filter(category=pk)
    except Exception as e:
        logger.exception(e)
    catgories = Category.objects.all()
    data = {
        'catgories': catgories,
        'films': films
    }
    return render(request, 'films/home.html', data)
