from django.core.management.base import BaseCommand

from services.clean_db import DataCleaner


class Command(BaseCommand):
    help = 'Clean movies by deleting all data in movies app'

    def handle(self, *args, **options):
        cleaner = DataCleaner()
        cleaner.clean()
        self.stdout.write(self.style.SUCCESS('Movies cleaned!'))
