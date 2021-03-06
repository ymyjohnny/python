# Register your models here.
#coding=utf-8

from django.contrib import admin
from .models import Question, Choice

#admin.site.register(Question)
#排版
# class QuestionAdmin(admin.ModelAdmin):
# 	fields = ['question_text','pub_date']
# 	#fields = ['pub_date', 'question_text']
# admin.site.register(Question, QuestionAdmin)

#添加Date information标签，并且折叠

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3
	
# class QuestionAdmin(admin.ModelAdmin):
# 	fieldsets = [
# 			(None,								{'fields': ['question_text']}),
# 			('Date information',	{'fields': ['pub_date'], 'classes':['collapse']}),			
# 			]
# 	inlines = [ChoiceInline]
	


class QuestionAdmin(admin.ModelAdmin):
		list_display = ('question_text', 'pub_date', 'was_published_recently')
		list_filter = ['pub_date']
		search_fields = ['question_text']
		date_hierarchy = 'pub_date'
	        fieldsets = [
                       (None,                                                          {'fields': ['question_text']}),
                       ('Date information',    {'fields': ['pub_date'], 'classes':['collapse']}),                      
                       ]
       		inlines = [ChoiceInline]
#admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)

