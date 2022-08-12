import json

from django.core.management.base import BaseCommand
from catbreadbot.api.models import BotResponse


class Command(BaseCommand):
    help = 'Autocomplete DB'

    def handle(self, *args, **kwargs):
        BotResponse.objects.all().delete()
        json_file = open('questions.json')
        data = json.load(json_file)
        for i, row in enumerate(data['rows']):
            new_row = BotResponse(id=i+1, text=row[1], message_yes=BotResponse.objects.all().filter(id=row[2]).first()
            if row[2] else None, message_no=BotResponse.objects.all().filter(id=row[3]).first() if row[3] else None)
            new_row.save()
