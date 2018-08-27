from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^session_words/', views.process),
    url(r'^session_words/words/', views.clear)
]