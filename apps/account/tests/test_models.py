from django.test import TestCase

from apps.account.models import User


class AuthorTestModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='Bob', last_name='Big')

    def test_first_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'Имя')
