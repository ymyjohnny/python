# Register your models here.

from django.contrib import admin

from .models import Question, Answer

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
    ]
    inlines = [AnswerInline]



class AnswerAdmin(admin.ModelAdmin):
    fields = ['answer_text', 'pub_date']
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Answer, AnswerAdmin)

