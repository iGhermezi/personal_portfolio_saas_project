from django.core.management.base import BaseCommand

from apps.portfolios_themes.models import PortfolioTemplate


TEMPLATES = [
    {
        'template_key': 'template_1',
        'name': 'Minimal Dark',
        'description': 'A modern dark portfolio with a clean developer-focused layout.',
        'access_level': PortfolioTemplate.ACCESS_FREE,
    },
    {
        'template_key': 'template_2',
        'name': 'Professional',
        'description': 'A structured professional portfolio for developers and professionals.',
        'access_level': PortfolioTemplate.ACCESS_FREE,
    },
    {
        'template_key': 'template_3',
        'name': 'Creative',
        'description': 'A creative portfolio layout with a stronger visual personality.',
        'access_level': PortfolioTemplate.ACCESS_VERIFIED,
    },
    {
        'template_key': 'template_4',
        'name': 'Executive',
        'description': 'A premium portfolio designed for experienced professionals.',
        'access_level': PortfolioTemplate.ACCESS_PREMIUM,
    },
    {
        'template_key': 'template_5',
        'name': 'Premium Showcase',
        'description': 'A premium showcase layout for a polished personal brand.',
        'access_level': PortfolioTemplate.ACCESS_PREMIUM,
    },
    {
    'template_key': 'arsam',
    'name': 'Arsam Template',
    'description': 'A cute strawberry-inspired kawaii portfolio with playful pastel details.',
    'access_level': PortfolioTemplate.ACCESS_PREMIUM,
    },
]


class Command(BaseCommand):
    help = 'Create or update the default portfolio templates.'

    def handle(self, *args, **options):
        for data in TEMPLATES:
            template, created = PortfolioTemplate.objects.update_or_create(
                template_key=data['template_key'],
                defaults={
                    'name': data['name'],
                    'description': data['description'],
                    'preview_img': '',
                    'access_level': data['access_level'],
                    'is_active': True,
                },
            )

            action = 'Created' if created else 'Updated'

            self.stdout.write(
                self.style.SUCCESS(
                    f'{action}: {template.name} ({template.template_key})'
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                'Default portfolio templates are ready.'
            )
        )