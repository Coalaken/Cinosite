from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required, permission_required
from django.http import StreamingHttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView

from .models import Film, Category
from .forms import FilmAddForm
from .services import open_file
from .tasks import change_bookmarks_status1, change_like_status1

@login_required(login_url="/login")
def home(request):
    if request.method == 'POST':
        film_name = request.POST.get("film-name")

        if film_name:
            change_bookmarks_status1.delay(request.user.username, film_name)
            # change_bookmarks_status.delay(request, Film, UserFilmRelation, film_name)


    films = Film.objects.select_related('added_by').all()
    catgories = Category.objects.all()
    data = {
        'catgories': catgories,
        'films': films
    }
    return render(request, 'films/home.html', data)
    
    
@login_required(login_url="/login")
def search(request):    
    if request.method == 'POST':
        film_name = request.POST.get("film-name")
        if film_name:
            change_bookmarks_status1.delay(request.user.username, film_name)
    films = Film.objects.select_related('added_by').\
        filter(name__icontains=request.GET.get("search"))
    catgories = Category.objects.all()
    data = {
        'catgories': catgories,
        'films': films
    }
    return render(request, 'films/home.html', data)
    

#############################################################
# something wrong ... 
class FilmCreateView(CreateView):
    template_name = 'films/add_film.html'
    form_class = FilmAddForm
    
    def form_valid(self, form):
        form.cleaned_data['added_by'] = self.request.user
        form.save()
        return super().form_valid(form)
#############################################################
        
        
@login_required(login_url='/login') 
def bookmarks(request):
    if request.method == 'POST':
        film_name = request.POST.get("film-name")
        if film_name:
            change_bookmarks_status1.delay(request.user.username, film_name)
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
    if request.method == 'POST':
        film_liked = request.POST.get("film-liked")
        if film_liked:
            change_like_status1.delay(request.user.username, film_liked)
    film = get_object_or_404(Film, pk=pk)
    catgories = Category.objects.all()
    data = {
        'catgories': catgories,
        'films': film
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
    films = Film.objects.filter(category=pk)
    catgories = Category.objects.all()
    data = {
        'catgories': catgories,
        'films': films
    }
    return render(request, 'films/home.html', data)