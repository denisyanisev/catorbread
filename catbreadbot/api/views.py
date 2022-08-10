from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from .models import Message, BotResponse
from .serializers import MessageSerializer, BotResponseSerializer


# Create new and list all messages only actions
class MessageViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        text = data['text'].lower()
        if text == '/start':
            serializer.save(bot_response=BotResponse.objects.last())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            message = self.queryset.filter(user_id=data['user_id']).first()
            if not message:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            parsed_message = any(map(lambda x: x in text, ['yes', 'да', 'yeah', 'ага']))  # this is temporary
            bot_response = getattr(message.bot_response, 'message_yes' if parsed_message else 'message_no')
            serializer.save(bot_response=bot_response)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class BotResponseViewSet(viewsets.ModelViewSet):
    queryset = BotResponse.objects.all()
    serializer_class = BotResponseSerializer

