from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answer
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render


# Create your views here.
#def index(request):
   # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #latest_question_list1 = Answer.objects.order_by('-pub_date')[:5]
    
    #output = ', '.join([p.question_text, for p in latest_question_list])
#    answer = ', '.join([a.answer_text, for a in latest_question_list1])
#    output = ', '.join([a.answer_text, for a in latest_question_list1])
   
    
   # return HttpResponse(output)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('bbsapp/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'bbsapp/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
