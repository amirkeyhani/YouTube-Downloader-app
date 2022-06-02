from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    # path('download/', views.download_video, name='download'),
    # path('', views.index, name='index'),
    path('', views.home.as_view(), name='home'),
]
