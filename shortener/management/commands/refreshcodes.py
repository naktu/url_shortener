from django.core.management.base import BaseCommand, CommandError
from shortener.models import ShortURL


class Command(BaseCommand):
    help = 'Refresh all url shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        return ShortURL.objects.refresh_short_codes(items=options['items'])

