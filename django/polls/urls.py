import re
from django.urls import path, re_path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),


    # re_path(r'^$', views.index, name='index')
    # re_path(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # # $가 없으면
    # # 정규표현식에서 뒤에 까지 다 포함을 해서 밑에 있는 애들이 동작을 안합니다.
    # #
    # re_path(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # re_path(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

    # re_path를 사용해서 정규표현식으로 구현해보세요
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    re_path(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    re_path(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

]

# re_path(r'(?P<pk>\d+)/$', views.post_detail),
