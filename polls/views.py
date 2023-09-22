from django.shortcuts import render, redirect
from django.http import HttpResponse
from polls.models import Questions
from django.contrib import messages


def index(request):
    all_question = Questions.objects.all
    return render(request, "index.html", {"all_question": all_question})

def detail(request, question_id):
    question = Questions.objects.get(id=question_id)
    context = {"question":question}
    if question.can_vote() is False:
        messages.error(request, 'This poll was close')
        return redirect('/')
    
    return render(request, 'detail.html', context)
