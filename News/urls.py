from django.contrib import admin
from django.urls import include, path

import polls.views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('news/', polls.views.news)
]