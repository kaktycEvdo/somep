from django.conf.urls import url

from . import views

app_name = "favlinks"
urlpatterns = [
    url(r'authorisation', views.authorisation),
    url(r'registration', views.registration),
    url(r'main', views.main),
    url(r'add', views.add),
    url(r'edit', views.edit),
    url(r'delete', views.delete),
    url(r'changecontent', views.change_content),
]
