from django.utils.timezone import now

from django.db import models


class Message(models.Model):
    user_id = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    bot_response = models.ForeignKey('BotResponse', models.SET_NULL, blank=True, null=True)
    parsed_answer = models.BooleanField(blank=True, null=True)
    created = models.DateTimeField(default=now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.text}'


class BotResponse(models.Model):
    text = models.CharField(max_length=300)
    message_yes = models.ForeignKey('BotResponse', models.SET_NULL, blank=True, null=True, related_name='messages_yes')
    message_no = models.ForeignKey('BotResponse', models.SET_NULL, blank=True, null=True, related_name='messages_no')

    def __str__(self):
        return f'id: {self.pk} {self.text}'
