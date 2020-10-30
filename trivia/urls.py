from django.urls import path
from .views import QuestionsView

urlpatterns = [
    path('', QuestionsView.as_view(), name='questions'),
]
