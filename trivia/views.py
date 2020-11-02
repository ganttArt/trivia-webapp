import json
import random
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.datastructures import MultiValueDictKeyError
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

        return render(request, self.template_name, {'form': form, 'questions': self.questions[:10]})

    def post(self, request, *args, **kwargs):
        answered_correctly = 0

        for i in range(1, len(request.POST)):
            try:
                if request.POST[str(i)] == self.questions[i - 1].correct_answer:
                    answered_correctly += 1
            except MultiValueDictKeyError:
                print('You skipped a question')

        return render(request, 'results.html',
                      {'answered_correctly':answered_correctly, 'questions': self.questions[:10]})
