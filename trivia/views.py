import json
import random
from django.shortcuts import render
from django.views.generic import TemplateView


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

        num = 1
        for question in self.questions:
            question.assign_number(str(num))
            print(question.number)
            num += 1
        
        self.questions = self.questions[:20]
        context['questions'] = self.questions
        return context
