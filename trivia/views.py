import json
import random
from django.shortcuts import render
from django.views.generic import TemplateView


class Question:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

        self.answers.append(correct_answer)
        random.shuffle(self.answers)


class QuestionsView(TemplateView):
    template_name = 'questions.html'
    questions = []

    with open('Apprentice_TandemFor400_Data.json') as file:
        data = json.load(file)
        for question in data:
            questions.append(
                Question(
                    question['question'],
                    question['incorrect'],
                    question['correct']
                )
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        random.shuffle(self.questions)
        self.questions = self.questions[:20]
        context['questions'] = self.questions
        return context
