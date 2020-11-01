from django import forms

class TriviaForm(forms.Form):
    question_1 = forms.CharField(max_length=150)
    question_2 = forms.CharField(max_length=150)
    question_3 = forms.CharField(max_length=150)
    question_4 = forms.CharField(max_length=150)
    question_5 = forms.CharField(max_length=150)
    question_6 = forms.CharField(max_length=150)
    question_7 = forms.CharField(max_length=150)
    question_8 = forms.CharField(max_length=150)
    question_9 = forms.CharField(max_length=150)
    question_10 = forms.CharField(max_length=150)
    