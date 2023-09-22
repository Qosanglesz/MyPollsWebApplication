from django.urls import path
from polls import views
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<question_id>', views.detail, name='detail'),
    path('vote/<question_id>', views.vote, name='vote'),
    path('result/<question_id>', views.result, name='result'),
]