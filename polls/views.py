from django.shortcuts import render, redirect
from django.urls import reverse
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

def vote(request, question_id):
    if request.method == 'POST':
        question = Questions.objects.get(id=question_id)
        selected_choice = question.choice_set.get(choice_text = request.POST.get('choice'))
        selected_choice.votes += 1
        selected_choice.save()
        return redirect(reverse('result', args=(question.id,)))
    
def result(request, question_id):
    return render(request, "result.html")
