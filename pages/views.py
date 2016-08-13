# -*- coding: utf-8 -*-
from django.utils import six
from django.http import Http404
from django.views.generic import DetailView
from .models import Page


class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'


used_slugs = set()


class PageMixinMetaclass(type):
    """
    Добавляет в список used_slugs все view в которых есть
    миксин PageMixin. Сделано чтобы страница не была
    доступна одновременно как статичная (page/<slug>) и
    как часть страницы к которой применен PageMixin
    """
    def __new__(cls, name, bases, attrs):
        view = super(PageMixinMetaclass, cls).__new__(cls, name, bases, attrs)
        global used_slugs

        if view.page_slug:
            used_slugs.add(view.page_slug)
        return view


class PageMixin(six.with_metaclass(PageMixinMetaclass)):
    """
    Mixin добавляет к контексту страницу с указанным page_slug
    """
    page_slug = None

    @property
    def page(self):
        if not hasattr(self, '_page'):
            if not self.page_slug:
                raise AttributeError(
                    "Page mixin detail view %s must using "
                    "with a page_slug." % self.__class__.__name__
                )
            try:
                page = Page.objects.get(slug=self.page_slug)
                if not page.active:
                    raise Http404
                self._page = page
            except Page.DoesNotExist:
                self._page = None
        return getattr(self, '_page')

    def get_context_data(self, **kwargs):
        context = super(PageMixin, self).get_context_data(**kwargs)
        context['page'] = self.page
        if not isinstance(self, DetailView):
            context['object'] = self.page
        return context
