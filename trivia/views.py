import json
import random
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.datastructures import MultiValueDictKeyError
from .forms import TriviaForm


class Question:
    def __init__(self, question, answers, correct_answer, question_id):
        self.question = question
        self.answers = answers
        self.answers.append(correct_answer)
        self.correct_answer = correct_answer
        self.question_id = question_id
    
    def add_correctness(self, correct):
        self.correct = correct

    def add_question_order(self, question_order):
        self.question_order = question_order


class QuestionsView(TemplateView):
    template_name = 'questions.html'
    questions = []
    trivia_form = TriviaForm

    with open('Apprentice_TandemFor400_Data.json') as file:
        data = json.load(file)
        question_id = 0
        print('loading questions')
        for question in data:
            questions.append(
                Question(
                    question['question'],
                    question['incorrect'],
                    question['correct'],
                    question_id
                )
            )
            question_id += 1    

    def get(self, request, *args, **kwargs):
        form = self.trivia_form()
        question_order = 1
        questions = random.sample(self.questions, 10)

        for question in questions:
            question.add_question_order(question_order)
            question_order += 1
        
        return render(request, self.template_name, {'form': form, 'questions': questions})

    def post(self, request, *args, **kwargs):
        answered_correctly = 0
        questions = []

        for answer in request.POST.items():
            correct = False
            if answer[0] == 'csrfmiddlewaretoken':
                continue
            elif self.questions[int(answer[0])].correct_answer == answer[1]:
                answered_correctly += 1
                correct = True

            question = Question(
                self.questions[int(answer[0])].question,
                [],
                self.questions[int(answer[0])].correct_answer,
                None
            )
            question.add_correctness(correct)
            questions.append(question)
            
        return render(request, 'results.html', {'answered_correctly':answered_correctly, 'questions': questions})
