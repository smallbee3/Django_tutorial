from django.shortcuts import render

from django.http import HttpResponse

# from django.polls.models import Question
# django 라는 같은 이름의 패키지에서 찾으려고해서 문제 발생.
from django.template import loader

from .models import Question


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

    # 가장 최근에 발행된 최대 4개의 Question목록
    latest_question_list = Question.objects.order_by('-pub_date')[:5]


    # 1) HttpResponse 방식
    # 쉼표 단위로 구분된 Question목록의 각 항목의 Question_text로 만들어진 문자열
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # 수업시간 실습 - 안보고 해보기 14:59
    context = {
        'latest_question_list': latest_question_list,
    }


    # 2) render 사용
    return render(request, 'polls/index.html', context)


    # 3) template을 명시적으로 불러와 rendering
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    # loader가 template를 불러오는 것.
    # 아래 render는 위와는 다르게 template안의 render임.


def detail(request, question_id):

    # return HttpResponse("You're looking at question %s." % question_id)

    question = Question.objects.get(pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)




def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)