# -*- coding: utf-8 -*-
from django.apps import apps
from helpers.models import ActivatableMixin, SlugTitleMixin, TextMixin
from .conf import PAGES_MODEL


class AbstractPage(ActivatableMixin, SlugTitleMixin, TextMixin):
    """
    Абстрактный класс для страницы
    """
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        abstract = True


if PAGES_MODEL:
    Page = apps.get_model(*PAGES_MODEL.split('.'))
else:
    class Page(AbstractPage):
        pass
