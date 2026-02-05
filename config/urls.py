from itertools import product

from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import include, path
from catalog import views

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("", include('catalog.urls', namespace='catalog')),
              ] + debug_toolbar_urls()
