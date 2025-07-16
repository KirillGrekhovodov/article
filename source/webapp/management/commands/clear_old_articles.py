from django.core.management import BaseCommand

from webapp.models import Article


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--date",
            type=str,
            help="Delete poll instead of closing it",
        )

    def handle(self, *args, **options):
        user_data_str = options.get("date")
        if user_data_str:
            articles = Article.objects.filter(created_at__date__lt=user_data_str)
            articles.delete()