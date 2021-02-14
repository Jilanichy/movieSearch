from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('^', include('movieclue.urls')),
    url('admin/', admin.site.urls),
]
