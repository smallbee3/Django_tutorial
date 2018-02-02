from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, Http404

# from django.polls.models import Question
# django 라는 같은 이름의 패키지에서 찾으려고해서 문제 발생.
from django.template import loader

from .models import Question, Choice


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

    # 2) 실습
    # question = Question.objects.get(pk=question_id)

    # 3) try ~ except문
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')

    # 4) short cut
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)


    # if request.method == 'POST':
    #     choice = request.POST['choice']
    #     return HttpResponse(choice)


    # 1번
    choice_pk = request.POST['choice']
    # print(type(choice_pk))
    choice = Choice.objects.get(pk=choice_pk)
    # pk 값에 str를 주던지

    choice.votes += 1
    choice.save()


    # 2번
    return redirect('polls:results', question_id=question_id)




def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

    # 박살
    # choice_pk = request.POST['choice']
    # choice = Choice.objects.get(pk=choice_pk)

    question = Question.objects.get(pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context)