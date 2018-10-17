# Example
Edit your urls.py module:

mysite/urls.py
```python
from django.contrib import admin
from django.urls import path, include
from django_home_urls import home

urlpatterns = [
    home('polls_index'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

polls/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='polls_index'),
]

```

Open your browser `http://127.0.0.1:8000/`, show `http://127.0.0.1:8000/polls/`.
