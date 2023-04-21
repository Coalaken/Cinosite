from django.shortcuts import get_object_or_404
from django.shortcuts import render


def change_bookmarks(request, model, relation_model, film_name):
    # film_name = request.POST.get("film-name")
    if film_name:
        try:
            film = model.objects.get(name=film_name)
        except Exception as e:
            print(e)
            pass
        else:
            if film:
                try:
                    relation = relation_model.objects.select_related('user').select_related('film').get(film=film, user=request.user)
                    if relation.in_bookmarks == True:
                        relation.in_bookmarks = False
                    else:
                        relation.in_bookmarks = True
                    relation.save()
                except Exception as e:
                    relation = relation_model.objects.create(
                        user=request.user,
                        film=film,
                        in_bookmarks=False)
                    relation.save()
    else:
        print("film name not exist")
        
        
def like(request, model, relation_model, film_liked):
    # film_liked = request.POST.get("film-liked")
    if film_liked:
        try:
            film = model.objects.get(name=film_liked)
        except Exception as e:
            print(e)
            pass
        else:
            if film:
                try:
                    relation = relation_model.objects.select_related('user').\
                        select_related('film').get(
                            film=film,
                            user=request.user
                            )
                    if relation.like == True:
                        relation.like = False
                    else:
                        relation.like = True
                    relation.save()
                except Exception as e:
                    relation = relation_model.objects.create(
                        user=request.user,
                        film=film,
                        in_bookmarks=False)
                    relation.save()
    else:
        print("film name not exist")

