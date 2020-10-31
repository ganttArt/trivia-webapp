import json
import random
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
# import .Apprentice_TandemFor400_Data as simplejson

class Question:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        
        self.answers = answers
        self.answers.append(correct_answer)
        random.shuffle(self.answers)

        self.correct_answer = correct_answer
        

class QuestionsView(TemplateView):
    template_name = 'questions.html'
    questions = [
        Question(
            "What was Tandem previous name?",
            ["Tandem", "Burger Shack", "Extraordinary Humans"],
            "Devmynd"
        ),
        Question(
            "In Shakespeare's play Julius Caesar, Caesar's last words were...",
            ["Iacta alea est!", "Vidi, vini, vici", "Aegri somnia vana"],
            "Et tu, Brute?"
        )
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = self.questions
        return context
