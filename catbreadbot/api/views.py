from rest_framework import generics, viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect
from .models import UserDialog, Questions
from .serializers import UserDialogSerializer, QuestionSerializer, MessageSerializer


class AddHistoryRow(generics.CreateAPIView):
    queryset = UserDialog.objects.all(),
    serializer_class = UserDialogSerializer


class UserHistory(viewsets.ViewSet):
    queryset = UserDialog.objects.all(),
    serializer_class = UserDialogSerializer

    def list(self, request):
        queryset = UserDialog.objects.all()
        serializer = UserDialogSerializer(queryset, many=True)
        return Response(serializer.data)


class ListQuestions(viewsets.ViewSet):
    queryset = Questions.objects.all(),
    serializer_class = QuestionSerializer

    def list(self, request):
        queryset = Questions.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)


class AddQuestion(generics.CreateAPIView):
    queryset = Questions.objects.all(),
    serializer_class = QuestionSerializer


class DialogView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'diaog.html'

    def get(self, request):
        user_id = request.query_params['user_id']
        question = UserDialog.objects.filter(user_id=user_id)
        if question:
            Response({'question': question, user_id: user_id})
        else:
            return Response({'question': Questions.objects.all()[3].question, user_id: user_id})
