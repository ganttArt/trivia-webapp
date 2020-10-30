from django.shortcuts import render
from django.views.generic import TemplateView


class QuestionsView(TemplateView):
    template_name = 'questions.html'
