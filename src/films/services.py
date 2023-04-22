from django.shortcuts import get_object_or_404
from django.shortcuts import render
from pathlib import Path
from typing import IO, Generator


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
                    relation = relation_model.objects.\
                        select_related('user').select_related('film').\
                            get(film=film, user=request.user)
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


def ranged(
        file: IO[bytes],
        start: int = 0,
        end: int = None,
        block_size: int = 8192,
) -> Generator[bytes, None, None]:
    consumed = 0

    file.seek(start)
    while True:
        data_length = min(block_size, end - start - consumed) if end else block_size
        if data_length <= 0:
            break
        data = file.read(data_length)
        if not data:
            break
        consumed += data_length
        yield data

    if hasattr(file, 'close'):
        file.close()


def open_file(request, model, video_pk):
    _video = get_object_or_404(model, pk=video_pk)

    path = Path(_video.video.path)

    file = path.open('rb')
    file_size = path.stat().st_size

    content_length = file_size
    status_code = 200
    content_range = request.headers.get('range')

    if content_range is not None:
        content_ranges = content_range.strip().lower().split('=')[-1]
        range_start, range_end, *_ = map(str.strip, (content_ranges + '-').split('-'))
        range_start = max(0, int(range_start)) if range_start else 0
        range_end = min(file_size - 1, int(range_end)) if range_end else file_size - 1
        content_length = (range_end - range_start) + 1
        file = ranged(file, start=range_start, end=range_end + 1)
        status_code = 206
        content_range = f'bytes {range_start}-{range_end}/{file_size}'

    return file, status_code, content_length, content_range