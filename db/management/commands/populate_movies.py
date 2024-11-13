from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from services.csv_mapper import MovieCSVParser
from services.db_importer import MovieDataImporter


class Command(BaseCommand):
    help = 'Populate movies with dataset csv file'

    def handle(self, *args, **kwargs):
        parser = MovieCSVParser(settings.MOVIES_FILENAME)
        movies_dto = parser.read_csv_and_map_to_dto()
        importer = MovieDataImporter(movies_dto)

        try:
            with transaction.atomic():
                importer.import_data()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error occurred: {e}'))
            raise e
        else:
            self.stdout.write(self.style.SUCCESS('Movies populated with csv data!'))
