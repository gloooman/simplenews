from django.contrib import admin
from django.urls import path, include
from users.views import verify
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('news.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path(r'^verify/(?P<uuid>[a-z0-9\-]+)/', verify, name='verify'),
    path(r'^tinymce/', include('tinymce.urls'))
]
