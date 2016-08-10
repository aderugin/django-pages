# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import PageDetailView

urlpatterns = [
    url(r'^pages/(?P<slug>[\w-]+)/$', PageDetailView.as_view(), name='page-detail')
]
