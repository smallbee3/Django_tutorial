from django.contrib import admin

# from django.polls.models import Question, Choice
# django라는 이름의 package가 있어서 못찾는 것.

from .models import Question, Choice



admin.site.register(Question)
admin.site.register(Choice)

