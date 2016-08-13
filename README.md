# Installation and setup

```
pip install git+git://github.com/aderugin/django-pages.git
```

```
# If you need specific page model, you have to define PAGES_MODEL

PAGES_MODEL = 'some_app.SomeModel'
```

```
# urls.py

urlpatterns = [
    ...
    url(r'^', include('pages.urls', namespace='pages')),
    ...
]
```

# Usage

```
# views.py
from pages.views import PageMixin

class SomeView(PageMixin, TemplateView):
    page_slug = 'some_page_slug'


# template
# add template pages/page_detail.html

{{ page.title }}
{{ page.text|safe }}
```
