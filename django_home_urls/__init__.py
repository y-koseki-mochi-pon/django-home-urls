name = "django_home_urls"

def home(view_name):
    from django.urls import path

    def f(request, *args, **kwargs):
        from django.urls import resolve, reverse
        path = reverse(view_name)
        func = resolve(path).func
        return func(request, *args, **kwargs)
    return path("", f)
