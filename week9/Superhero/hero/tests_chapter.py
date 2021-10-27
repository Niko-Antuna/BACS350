from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Hero, Chapter


class ChapterDataTest(TestCase):

    def setUp(self):
        self.hero_title = 'Iliad'
        self.chapter1 = dict(hero=self.hero_title,
                             hero='Achilles', order='1', artcile='1.md')
        self.chapter2 = dict(hero=self.hero_title,
                             hero='Agamememnon', order='2', article='2.md')

    def test_add_chapter(self):
        self.assertEqual(len(Chapter.objects.all()), 0)
        Chapter.objects.create(**self.chapter1)
        Chapter.objects.create(**self.chapter2)
        self.assertEqual(len(Chapter.objects.all()), 2)
