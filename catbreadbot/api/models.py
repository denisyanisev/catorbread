from django.utils.timezone import now

from django.db import models


class UserDialog(models.Model):
    user_id = models.CharField(max_length=200)
    question = models.ForeignKey('Questions', models.SET_NULL, blank=True, null=True)
    user_answer = models.CharField(max_length=200)
    parsed_answer = models.BooleanField()
    created = models.DateTimeField(default=now)

    # objects = models.Manager()


class Questions(models.Model):
    question = models.CharField(max_length=300)
    answer_yes = models.ForeignKey('Questions', models.SET_NULL, blank=True, null=True, related_name='answers_yes')
    answer_no = models.ForeignKey('Questions', models.SET_NULL, blank=True, null=True, related_name='answers_no')

