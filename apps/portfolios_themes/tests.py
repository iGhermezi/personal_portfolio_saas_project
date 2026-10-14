from django.test import TestCase

from .models import PortfolioTemplate


class PortfolioTemplateTests(TestCase):

	def test_template_can_be_created_without_legacy_preview_img(self):
		template = PortfolioTemplate.objects.create(
			name='New template',
			description='Template description',
		)

		self.assertIsNotNone(template.pk)
		self.assertFalse(template.preview_image)
