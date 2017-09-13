from django.conf.urls import url
from . import views

app_name="question"

urlpatterns = [
    url(r'^$', views.question_list, name='question_list'),
    url(r'^question/new/$', views.question_new, name='question_new'),
    url(r'^(?P<ques_id>[0-9]+)/$', views.details, name="details"),
    url(r'^add_ans/$', views.add_ans, name="add_ans"),
    url(r'^add_ques/$', views.add_ques, name="add_ques"),
]