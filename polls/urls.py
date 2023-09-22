from django.urls import path
from polls import views
urlpatterns = [
    path('', views.index),
    path('detail/<question_id>', views.detail)
]