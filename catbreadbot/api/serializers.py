from .models import Message, BotResponse
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    bot_response = serializers.PrimaryKeyRelatedField(read_only=True)

    def save(self, **kwargs):
        super().save(**kwargs)

    class Meta:
        model = Message
        fields = ['id', 'user_id', 'text', 'bot_response']


class BotResponseSerializer(serializers.ModelSerializer):
    message_yes = serializers.PrimaryKeyRelatedField(queryset=BotResponse.objects.all(), allow_null=True)
    message_no = serializers.PrimaryKeyRelatedField(queryset=BotResponse.objects.all(), allow_null=True)

    class Meta:
        model = BotResponse
        fields = ['id', 'text', 'message_yes', 'message_no']
