from .models import UserDialog, Questions
from rest_framework import serializers


class UserDialogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDialog
        fields = ['user_id', 'question', 'user_answer', 'parsed_answer']
        # fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['question', 'answer_yes', 'answer_no']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDialog
        fields = ['user_id', 'user_answer']

