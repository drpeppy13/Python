from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create), #localhost:8000/create
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^(?P<number>\d+)/delete$', views.destroy),
]

def printName(x):
    print x


# blogs app
# / - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'.
# /new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'.
# /create - Have this be handled by a method named 'create'.  For now, have this url redirect to /.
# /{{number}} - display 'placeholder to display blog {{number}}'.  For example /15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.
# /{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'.
# /{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /. 

printName("Minh")