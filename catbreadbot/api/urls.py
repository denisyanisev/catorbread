from django.urls import path
from catbreadbot.api.views import AddHistoryRow, UserHistory, AddQuestion, ListQuestions, DialogView


urlpatterns = [
    path('chat/', DialogView.as_view(), name='send-message'),
    path('create/', AddHistoryRow.as_view(), name='create-row'),
    path('create-question/', AddQuestion.as_view(), name='create-question-row'),
    # path('update/<int:pk>/', UpdateQuestion.as_view(), name='update-question-row'),
    path('history/', UserHistory.as_view({'get': 'list'})),
    path('questions/', ListQuestions.as_view({'get': 'list'})),
    # path('/dialog', ),
]
