from django.urls import path, re_path

from .import views
urlpatterns = [
    # re_path(r'^about', views.about, name='about'),
    # re_path(r'^contact', views.contact, name='contact'),
    # re_path(r'^products/(?P<productid>\d+)/', views.product),
    # re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
    # path('details/', views.details),
    path('', views.index, name='index'),
    path('about/', views.about, name='about')

]