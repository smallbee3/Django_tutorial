import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        '''
        이 Question의 게시일자가 현재시각에서 1일 전보다 이후인지
           (Question을 게시한지 1일이 지나지 않았는지)

        :return:
        '''
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    # timedelta 1은 하루 단위.
    #

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # 데이터베이스에서 저장할 때도 type이 있음.
    # 양수, 음수, 날짜, 시간 etc -> 데이터를 효율적으로 관리 가능

    # 클래스를 선언하고 클래스 속성을 얹고 하는거랑 다르게 동작. 이렇게 핳는건
    # 클래스랑 데이터베이스의 로우랑 똑같이.


    def __str__(self):
        return '{} | {}'.format(
            self.question.question_text,
            self.choice_text,
        )