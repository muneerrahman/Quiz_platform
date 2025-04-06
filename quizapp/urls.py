
from django.urls import path
from .views import CreateQuizView, AddQuestionView, AddOptionView, QuestionDetailView, QuizSubmissionView, \
    UserSubmissionHistoryView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/quiz/create/', CreateQuizView.as_view(), name='create-quiz'),
    path('admin/quiz/<int:quiz_id>/add-question/', AddQuestionView.as_view(), name='add-question'),
    path('admin/question/<int:question_id>/add-option/', AddOptionView.as_view(), name='add-option'),
    path("questions/<int:pk>/", QuestionDetailView.as_view()),
    path('submit-quiz/', QuizSubmissionView.as_view(), name='submit-quiz'),
    path('my-submissions/', UserSubmissionHistoryView.as_view(), name='user-submissions'),
]
