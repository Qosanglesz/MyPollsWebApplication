from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Questions

def index(request):
    all_question = Questions.objects.all
    return render(request, "index.html", {"all_question": all_question})

def detial(request, question_id):
    return render(request, 'detial.html')