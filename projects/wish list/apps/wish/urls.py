from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^wish_item/create$', views.create_wish),
    url(r'^wish_item/add$', views.add_wish),
    url(r'^wish_item/add/(?P<wish_id>\d+)$', views.join_wish),
    url(r'^wish_item/(?P<wish_id>\d+)$', views.show_wish),
    url(r'^wish_item/remove/(?P<wish_id>\d+)$', views.remove_wish),
    url(r'^wish_item/delete/(?P<wish_id>\d+)$', views.delete_wish),
    url(r'^logout$', views.logout),
]
