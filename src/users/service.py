def register_form_checker(form):
    if form.is_valid():
        the_form = form.save()