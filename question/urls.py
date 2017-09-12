from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.question_list, name='question_list'),
    url(r'^question/new/$', views.question_new, name='question_new'),
]