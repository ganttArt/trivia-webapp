import json
import random
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import TriviaForm


class Question:
    def __init__(self, question, answers, correct_answer, number=0):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
        self.number = number

        self.answers.append(correct_answer)
        random.shuffle(self.answers)
    
    def assign_number(self, number):
        self.number = number


class QuestionsView(TemplateView):
    template_name = 'questions.html'
    questions = []
    trivia_form = TriviaForm

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

    def get(self, request, *args, **kwargs):
        form = self.trivia_form()
        random.shuffle(self.questions)

        num = 1
        for question in self.questions:
            question.assign_number(str(num))
            num += 1

        return render(request, self.template_name, {'form': form, 'questions': self.questions[:20]})

    def post(self, request, *args, **kwargs):
        form = self.trivia_form(request.POST)
        print(request.POST)
        if form.is_valid():
            print('valid')
            return render(request, 'results.html', {'result':request.POST})