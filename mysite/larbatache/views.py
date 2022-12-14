from django.shortcuts import render
from .models import Question
from django.template import loader
from django.shortcuts import render
from django.http import Http404


# Create your views here.
from django.http import HttpResponse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('larbatache/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def test(request):
    template = loader.get_template('larbatache/test.html')
    context = {
    }
    return HttpResponse(template.render(context,request))


