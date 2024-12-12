import json
from django.core.management.base import BaseCommand
from app.models import DeAddictionCenter

class Command(BaseCommand):
    help = 'Load de-addiction centers data from dataset.json'

    def handle(self, *args, **kwargs):
        try:
            with open('dataset.json', 'r') as file:
                data = json.load(file)
                for entry in data:
                    DeAddictionCenter.objects.create(
                        state=entry['state'],
                        district=entry['district'],
                        ngo_name=entry['ngo_name'],
                        address=entry['address'],
                        bed_capacity=entry['bed_capacity']
                    )
                self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('dataset.json file not found.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))
