from django.contrib import admin
from django.urls import path

# importing views from views..py
from .views import jpgtopdf
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
	path('upload/', jpgtopdf),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)