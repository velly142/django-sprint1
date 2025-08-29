from . import views
from django.urls import path

app_name = 'pages'

urlpatterns = [
    path('rules/', views.rules, name='rules'),
    path('about/', views.about, name='about'),
]
