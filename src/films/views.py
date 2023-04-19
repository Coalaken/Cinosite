from django.shortcuts import render

from .models import Film, FilmData, UserFilmRelation


def home(request):
    if request.method == 'POST':
        film_name = request.POST.get("film-name")
        if film_name:
            try:
                film = Film.objects.get(name=film_name)
            except Exception as e:
                print(e)
                pass
            else:
                if film:
                    try:
                        relation = UserFilmRelation.objects.select_related('user').select_related('film').get(film=film, user=request.user)
                        if relation.in_bookmarks == True:
                            relation.in_bookmarks = False
                        else:
                            relation.in_bookmarks = True
                        relation.save()
                    except Exception as e:
                        relation = UserFilmRelation.objects.create(
                            user=request.user,
                            film=film,
                            in_bookmarks=False)
                        relation.save()
        else:
            print("film name not exist")
        films = Film.objects.select_related('data').prefetch_related('viewers').all()
        data = {
            'films': films
        }
        return render(request, 'films/home.html', data)
    else:
        films = Film.objects.select_related('data').prefetch_related('viewers').all()
        data = {
            'films': films
        }
        return render(request, 'films/home.html', data)
    

def search(request):
    pass
