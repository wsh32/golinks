from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:short_link>/edit', views.edit, name='edit'),
    path('<str:short_link>/set', views.set_link, name='set'),
    path('<str:short_link>', views.forward, name='forward'),
]
