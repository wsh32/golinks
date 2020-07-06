from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<str:short_link>/edit', views.edit_view, name='edit'),
    path('<str:short_link>/set', views.set_link_view, name='set'),
    path('<str:short_link>', views.forward_view, name='forward'),
    path('int/login', views.login_view, name='login'),
    path('int/logout', views.logout_view, name='logout'),
    path('int/auth', views.auth_view, name='auth'),
]
