from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^travels$', views.dashboard),
    url(r'^travels/create$', views.create_destination),
    url(r'^travels/add$', views.add_destination),
    url(r'^travels/destination/(?P<trip_id>\d+)$', views.show_trip),
    url(r'^travels/destination/join/(?P<trip_id>\d+)$', views.join_trip),
    url(r'^logout$', views.logout),
]
