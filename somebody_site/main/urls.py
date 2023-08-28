from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home),
    path('page1/', views.page1, name="myform"),
    path('page2/', views.page2),
    path(r'page2/<slug:slug>/', views.page2),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
