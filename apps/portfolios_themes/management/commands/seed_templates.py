from django.core.management.base import BaseCommand
from apps.portfolios_themes.models import PortfolioTemplate


TEMPLATES = [
    {
        'template_key': 'arsam',
        'name': 'Arsam',
        'description': (
            'A playful strawberry-kawaii portfolio with soft pastel '
            'cards and cute details.'
        ),
        'preview_img': '',
        'access_level': PortfolioTemplate.ACCESS_PREMIUM,
    },
    {
        'template_key': 'template_2',
        'name': 'Minimal Dark',
        'description': (
            'A clean dark portfolio with modern typography, '
            'subtle borders and violet accents.'
        ),
        'preview_img': '',
        'access_level': PortfolioTemplate.ACCESS_FREE,
    },
    {
        'template_key': 'template_3',
        'name': 'Creative Brutalist',
        'description': (
            'A bold brutalist portfolio with expressive typography, '
            'strong borders and playful composition.'
        ),
        'preview_img': '',
        'access_level': PortfolioTemplate.ACCESS_PREMIUM,
    },
    {
        'template_key': 'template_4',
        'name': 'Editorial',
        'description': (
            'An elegant editorial portfolio inspired by magazine '
            'layouts and refined typography.'
        ),
        'preview_img': '',
        'access_level': PortfolioTemplate.ACCESS_PREMIUM,
    },
    {
        'template_key': 'template_5',
        'name': 'Developer Terminal',
        'description': (
            'A developer-focused portfolio inspired by terminal '
            'interfaces and code editors.'
        ),
        'preview_img': '',
        'access_level': PortfolioTemplate.ACCESS_PREMIUM,
    },

    {
    "name": "Emerald Signature",
    "description": "A dark creative portfolio with an elegant emerald accent.",
    "preview_img": "",
    "template_key": "template_6",
    "access_level": PortfolioTemplate.ACCESS_VERIFIED,
    "is_active": True,
    },
]


class Command(BaseCommand):
    help = 'Seed the default portfolio templates.'

    def handle(self, *args, **options):
        for template_data in TEMPLATES:
            template_key = template_data['template_key']

            PortfolioTemplate.objects.update_or_create(
                template_key=template_key,
                defaults={
                    'name': template_data['name'],
                    'description': template_data['description'],
                    'preview_img': template_data['preview_img'],
                    'access_level': template_data['access_level'],
                    'is_active': True,
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                'Portfolio templates seeded successfully.'
            )
        )