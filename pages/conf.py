# -*- coding: utf-8 -*-
from django.conf import settings

PAGES_MODEL = getattr(settings, 'PAGES_MODEL', None)
